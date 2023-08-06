from copy import deepcopy
from easyadmin import Admin, buttons, forms, html_input, row, card, modal, admin
from fastapi.responses import HTMLResponse
from fastapi import HTTPException

async def frontend_setup(server):

    log = server.log

    admin_gui = server.api_routers[1]
    admin_prefix = server.ADMIN_PREFIX

    server.admin = Admin(
        title=server.server.title,
        title_link = admin_prefix,
        side_bar_sections = [
            {
                'items': [
                    {
                        'name':  'Users',
                        'href': f'{admin_prefix}/users',
                        'icon': 'user',
                        'items': []
                    },
                    {
                        'name':  'Services',
                        'href': f'{admin_prefix}/services',
                        'icon': 'robot',
                        'items': []
                    },
                    {
                        'name':  'Groups',
                        'href': f'{admin_prefix}/groups',
                        'icon': 'users',
                        'items': []
                    },
                    {
                        'name':  'Roles',
                        'href': f'{admin_prefix}/roles',
                        'icon': 'bezier-curve',
                        'items': []
                    },
                    {
                        'name':  'Actions',
                        'href': f'{admin_prefix}/actions',
                        'icon': 'id-badge',
                        'items': []
                    }
                ]
            },
            {
                'items': [
                    {
                        'name':  'Tokens Issued',
                        'href': f'{admin_prefix}/tokens',
                        'icon': 'key',
                        'items': []
                    }
                ]
            }
        ]
    )

    logout_modal = modal.get_modal(
        f'logoutModal',
        alert='Ready to Leave',
        body=buttons.get_button(
            'Go Back',
            color='success', 
            href=f'{admin_prefix}/'
        ) + 
        buttons.get_button(
            'Log out',
            color='danger',
            href=f'/logout'
        ),
        footer='',
        size='sm'
    )

    @admin_gui.get('/', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_home(access_token=None):
        return await _admin_users(access_token)
    @admin_gui.post('/', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def re_admin_users(access_token=None):
        return await _admin_users(access_token)

    @admin_gui.get('/users', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_users(access_token=None):
        return await _admin_users(access_token)
    
    @admin_gui.get('/services', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_users(access_token=None):
        return await _admin_users(access_token, account_type='service')

    @admin_gui.get('/user/{username}', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_user_page(username: str, access_token: str = None):
        users = await server.auth_users.select(
            'username', where={'username': username}
        )
        if not users:
            raise HTTPException(
                status_code=404,
                detail=f"No User with name {username} exists"
            )
            
        groups = await server.auth_groups.select('group_name')
        groups = deepcopy([group['group_name'] for group in groups])

        user_page = admin.get_admin_page(
            name=username, 
            sidebar=server.admin.sidebar,
            body=await get_user_details(username, groups),
            current_user=access_token['permissions']['users'][0],
            modals=logout_modal
        )
        return user_page

    @admin_gui.get('/service/{username}', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_service_page(username: str, access_token: str = None):
        users = await server.auth_users.select(
            'username', where={'username': username}
        )
        if not users:
            raise HTTPException(
                status_code=404,
                detail=f"No Service with name {username} exists"
            )
            
        groups = await server.auth_groups.select('group_name')
        groups = deepcopy([group['group_name'] for group in groups])

        user_page = admin.get_admin_page(
            name=username, 
            sidebar=server.admin.sidebar,
            body=await get_user_details(username, groups),
            current_user=access_token['permissions']['users'][0],
            modals=logout_modal
        )
        return user_page


    async def get_user_details(username: str, all_groups: list):

        details = await server.get_user_details(username)

        update_form = forms.get_form(
            f'Update {username}',
            [
                html_input.get_text_input("username", value=username),
                html_input.get_text_input("password", input_type='password') 
                if details['account_type'] == 'user' else '',
                html_input.get_text_input("email", value=details['email']) + 
                html_input.get_text_input("full_name", value=details['full_name'])
                if details['account_type'] == 'user' else '',
                html_input.get_checkbox('groups', [
                    (group, True) for group in details['groups']['groups'] ] +
                    [(group, False) for group in all_groups if not group in details['groups']['groups']]
                    )
            ],
            submit_name='update user',
            method='post',
            action=f'/auth/user/{username}'
        )
        groups, roles, actions = [], [], [] 
        if 'groups' in details['permissions']:
            groups = [group for group in details['permissions']['groups']]
        if 'roles' in details['permissions']:
            roles = [role for role in details['permissions']['roles']]
        if 'actions' in details['permissions']:
            actions = [action for action in details['permissions']['actions']]

        modal_row = row.get_row(
            card.get_card(
                f'{username}',
                update_form,
                size=12
            )+
            card.get_card(
                f"Groups",
                ''.join([
                    buttons.get_button(
                        group,
                        color='success', 
                        href=f'{admin_prefix}/group/{group}'
                    ) for group in groups
                ]),
                size=4
            )+
            card.get_card(
                f"Roles",
                ''.join([
                    buttons.get_button(
                        role,
                        color='success', 
                        href=f'{admin_prefix}/role/{role}'
                    ) for role in roles
                ]),
                size=4
            )+
            card.get_card(
                f"Actions",
                ''.join([
                    buttons.get_button(
                        action,
                        color='success', 
                        href=f'{admin_prefix}/action/{action}'
                    ) for action in actions
                ]),
                size=4
            )
        )
        return modal_row

    
    async def _admin_users(access_token: str, account_type='user'):
        users = await server.auth_users.select(
            'username', 'full_name', 'email', 'account_type', 'groups',
            where={'account_type': account_type}
        )
        users = users.copy()
        
        groups = await server.auth_groups.select('group_name')
        groups = deepcopy([group['group_name'] for group in groups])
        modals = [logout_modal]

        users_table = deepcopy(users)

        for ind, user in enumerate(users):
            username = user['username']
            modals.append(
                modal.get_modal(
                    f'delete{username}Modal',
                    alert='',
                    body=forms.get_form(
                        f'Delete {account_type} {username}',
                        [
                            buttons.get_button(
                                'Go Back',
                                color='success', 
                                href=f'{admin_prefix}/'
                        )],
                        submit_name=f'delete {account_type}',
                        method='delete',
                        action=f'/auth/user?username={username}'
                    ),
                    footer='',
                    size='sm'
                )
            )
            modals.append(
                modal.get_modal(
                    f'view_{username}',
                    alert='',
                    body=await get_user_details(username, groups),
                    footer='',
                    size='lg'
            ))
            if account_type == 'service':
                modals.append(
                    modal.get_modal(
                        f'generate{username}TokenModal',
                        alert='',
                        body=forms.get_form(
                            f'Generate {username} token',
                            [
                                buttons.get_button(
                                    'Go Back',
                                    color='success', 
                                    href=f'{admin_prefix}/'
                            )],
                            submit_name=f'Create Token',
                            method='get',
                            action=f'/auth/serviceaccount/token/{username}'
                        ),
                        footer='',
                        size='sm'
                    )
                )
            users_table[ind]['groups'] = ''.join([
                buttons.get_button(group, color='success', href=f'{admin_prefix}/group/{group}')
                for group in users_table[ind]['groups']['groups']
            ])
            actions = ( 
                    buttons.get_split_button(
                        f'view/edit',
                        icon='eye',
                        modal=f'view_{username}'
                    ) + 
                    buttons.get_split_button(
                        f'delete', 
                        modal=f'delete{username}Modal', 
                        color='danger',
                        icon='trash'
                    )
                )
            if account_type == 'service':
                token_button = buttons.get_split_button(
                        f'generate token', 
                        modal=f'generate{username}TokenModal', 
                        color='warning',
                        icon='key'
                    )
                actions = actions + token_button
            users_table[ind][' '] = actions

        email_and_full_name_input = html_input.get_text_input("email") + html_input.get_text_input("full_name")
        
        users_default = [{
            f'{account_type}': f"No {account_type}'s created yet",
        }]

        return server.admin.table_page(
            f'{account_type}s',
            users_table if len(users_table) > 0 else users_default,
            current_user=access_token['permissions']['users'][0],
            modals=''.join(modals),
            above="",
            below=forms.get_form(
                f'Create {account_type}',
                [
                    html_input.get_text_input("username"),
                    html_input.get_text_input("password", input_type='password')
                    if account_type =='user' else '',
                    email_and_full_name_input if account_type =='user' else '' ,
                    html_input.get_checkbox('groups', [(group, False) for group in deepcopy(groups)])
                ],
                submit_name=f'create {account_type}',
                method='put',
                action=f'/auth/{account_type}'
            )
        )

    async def get_group_details(group_name: str):
        group = await server.auth_groups.select(
            '*', where={'group_name': group_name}
        )
        if not group:
            raise HTTPException(
                status_code=404,
                detail=f"No Group with name {group_name} exists"
            )
        group = group[0]

        all_roles = await server.auth_roles.select('role')
        all_roles = [role['role'] for role in all_roles]

        roles = group['roles']['roles'] if isinstance(group['roles'], dict) else group['roles'] 
        roles = [role for role in roles if role in all_roles]

        permissions = []
        all_actions = await server.auth_actions.select('action')
        all_actions = [action['action'] for action in all_actions]
        for role in roles:
            actions = await server.auth_roles.select(
                'permissions', where={'role': role}
            )
            for action in actions.copy():
                if isinstance(action['permissions'], dict):
                    action['permissions'] = action['permissions']['actions']
                for action in action['permissions']:
                    if action in all_actions:
                        permissions.append(action)

        users = await server.auth_users.select('username', 'groups')
        for user in users.copy():
            if isinstance(user['groups'], dict):
                user['groups'] = user['groups']['groups']
        users = [user['username'] for user in users if group_name in user['groups']]

        roles_in_group = [
            (role, True) for role in roles] + [
            (role, False) for role in all_roles if not role in roles
        ]
        update_form = forms.get_form(
            f'Update {group_name}',
            [
                html_input.get_text_input("group_name", value=group_name),
                html_input.get_checkbox(
                    'roles',
                    roles_in_group
                ) if len(roles_in_group) > 0 else "No Roles"
            ],
            submit_name='update group',
            method='post',
            action=f'/auth/group/{group_name}'
        )

        modal_row = row.get_row(
            card.get_card(
                f'{group_name}',
                update_form,
                size=12
            )+
            card.get_card(
                f"Users",
                ''.join([
                    buttons.get_button(
                        user,
                        color='success', 
                        href=f'{admin_prefix}/user/{user}'
                    ) for user in users
                ]),
                size=4
            )+
            card.get_card(
                f"Roles",
                ''.join([
                    buttons.get_button(
                        role,
                        color='success', 
                        href=f'{admin_prefix}/role/{role}'
                    ) for role in roles
                ]),
                size=4
            )+
            card.get_card(
                f"Actions",
                ''.join([
                    buttons.get_button(
                        action,
                        color='success', 
                        href=f'{admin_prefix}/action/{action}'
                    ) for action in permissions
                ]),
                size=4
            )
        )
        return modal_row


    @admin_gui.get('/group/{group_name}', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_group_page(group_name: str, access_token: str = None):
        group = await server.auth_groups.select(
            '*', where={'group_name': group_name}
        )
        if not group:
            raise HTTPException(
                status_code=404,
                detail=f"No Group with name {group@_name} exists"
            )

        group_page = admin.get_admin_page(
            name=group, 
            sidebar=server.admin.sidebar,
            body=await get_group_details(group_name),
            current_user=access_token['permissions']['users'][0],
            modals=logout_modal
        )
        return group_page

    @admin_gui.get('/groups', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_groups(access_token=None):
        groups = await server.auth_groups.select('*')

        groups = groups.copy()
        roles = await server.auth_roles.select('role')

        roles = deepcopy([role['role'] for role in roles])
        modals = [logout_modal]

        groups_table = deepcopy(groups)
        for ind, group in enumerate(groups):
            group_name = group['group_name']
            if isinstance(group['roles'], dict):
                group['roles'] = group['roles']['roles']
                modals.append(modal.get_modal(
                    f'delete{group_name}Modal',
                    alert='',
                    body=forms.get_form(
                        f'Delete Group {group_name}',
                        [
                            buttons.get_button(
                                'Go Back',
                                color='success', 
                                href=f'{admin_prefix}/groups'
                        )],
                        submit_name='delete group',
                        method='delete',
                        action=f'/auth/group?group_name={group_name}'
                    ),
                    footer='',
                    size='sm'
                )
            )
            modals.append(modal.get_modal(
                f'view_{group_name}',
                alert='',
                body=await get_group_details(group_name),
                footer='',
                size='lg'
            ))
            groups_table[ind]['roles'] = ''.join([
                buttons.get_button(
                    role,
                    color='success', 
                    href=f'{admin_prefix}/role/{role}')
                for role in group['roles'] if role in roles
            ])

            actions = ( 
                buttons.get_split_button(
                    f'view/edit',
                    icon='eye',
                    modal=f'view_{group_name}'
                ) + 
                buttons.get_split_button(
                    f'delete',
                    color='danger',
                    modal=f'delete{group_name}Modal',
                    icon='trash'
                )
            )
            groups_table[ind][' '] = actions

        admin_table =  server.admin.table_page(
            'Groups',
            groups_table if len(groups_table) > 0 else [{'group_name': 'NO GROUPS', 'roles': ''}],
            current_user=access_token['permissions']['users'][0],
            modals=''.join(modals),
            above="",
            below=forms.get_form(
                'Create Group',
                [
                    html_input.get_text_input("group_name"),
                    html_input.get_checkbox('roles', [(role, False) for role in roles])
                ],
                submit_name='create group',
                method='put',
                action='/auth/group'
            )
        )
        return admin_table


    async def get_role_details(role_name: str):
        role = await server.auth_roles.select(
            '*', where={'role': role_name}
        )
        if not role:
            raise HTTPException(
                status_code=404,
                detail=f"No Role with name {role_name} exists"
            )
        role = role[0]

        permissions = role['permissions']['actions'] if isinstance(role['permissions'], dict) else role['permissions']
        all_actions = await server.auth_actions.select('action')
        all_actions = [action['action'] for action in all_actions]

        permissions = [action for action in permissions if action in all_actions]

        all_groups = await server.auth_groups.select('group_name', 'roles')
        for group in all_groups.copy():
            if isinstance(group['roles'], dict):
                group['roles'] = group['roles']['roles']

        groups = [group['group_name'] for group in all_groups if role_name in group['roles']]

        all_users = await server.auth_users.select('username', 'groups')
        users = []
        for user in all_users.copy():
            if isinstance(user['groups'], dict):
                user['groups'] = user['groups']['groups']
        for user in all_users:
            for group in user['groups']:
                if group in groups:
                    users.append(user['username'])
                    break
        actions_in_role = [
            (action, True) for action in permissions] + [
            (action, False) for action in all_actions if not action in permissions
        ]
        update_form = forms.get_form(
            f'Update {role_name}',
            [
                html_input.get_text_input("role", value=role_name),
                html_input.get_checkbox(
                    'actions', 
                    actions_in_role
                ) if len(actions_in_role) > 0 else "no actions"
            ],
            submit_name='update role',
            method='post',
            action=f'/auth/role/{role_name}'
        )

        modal_row = row.get_row(
            card.get_card(
                f'{role_name}',
                update_form,
                size=12
            )+
            card.get_card(
                f"Users",
                ''.join([
                    buttons.get_button(
                        user,
                        color='success', 
                        href=f'{admin_prefix}/user/{user}'
                    ) for user in users
                ]),
                size=4
            )+
            card.get_card(
                f"Groups",
                ''.join([
                    buttons.get_button(
                        group,
                        color='success', 
                        href=f'{admin_prefix}/group/{group}'
                    ) for group in groups
                ]),
                size=4
            )+
            card.get_card(
                f"Actions",
                ''.join([
                    buttons.get_button(
                        action,
                        color='success', 
                        href=f'{admin_prefix}/action/{action}'
                    ) for action in permissions
                ]),
                size=4
            )
        )
        return modal_row

    @admin_gui.get('/role/{role_name}', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_role_page(role_name: str, access_token=None):
        role = await server.auth_roles.select(
            'role', where={'role': role_name}
        )
        if not role:
            raise HTTPException(
                status_code=404,
                detail=f"No Role with name {role_name} exists"
            )
        role_page = admin.get_admin_page(
            name=role_name, 
            sidebar=server.admin.sidebar,
            body=await get_role_details(role_name),
            current_user=access_token['permissions']['users'][0],
            modals=logout_modal
        )
        return role_page
        

    @admin_gui.get('/roles', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_roles(access_token=None):
        roles = await server.auth_roles.select('*')
        roles = roles.copy()
        permissions = await server.auth_actions.select('action')
        permissions = [action['action'] for action in permissions]
        modals = [logout_modal]
        for role in roles:
            role_name = role['role']
            modals.append(modal.get_modal(
                f'delete{role_name}Modal',
                alert='',
                body=forms.get_form(
                    f'Delete Role {role_name}',
                    [
                        buttons.get_button(
                            'Go Back',
                            color='success', 
                            href=f'{admin_prefix}/groups'
                    )],
                    submit_name='delete role',
                    method='delete',
                    action=f'/auth/role?role={role_name}'
                ),
                footer='',
                size='sm'
            ))
            modals.append(modal.get_modal(
                f'view_{role_name}',
                alert='',
                body=await get_role_details(role_name),
                footer='',
                size='lg'
            ))
            role['permissions'] = role['permissions']['actions']
            role['permissions'] = ''.join([
                buttons.get_button(
                    action,
                    color='success', 
                    href=f'{admin_prefix}/action/{action}')
                for action in role['permissions'] if action in permissions
            ])

            actions = ( 
                    buttons.get_split_button(
                        f'view/edit',
                        icon='eye',
                        modal=f'view_{role_name}'
                    ) + 
                    buttons.get_split_button(
                        f'delete', 
                        modal=f'delete{role_name}Modal', 
                        color='danger',
                        icon='trash'
                    )
                )
            role[' '] = actions
        admin_table = server.admin.table_page(
            'Roles',
            roles if len(roles) > 0 else [{'role': 'no roles', 'actions': ''}],
            current_user=access_token['permissions']['users'][0],
            modals=''.join(modals),
            above="",
            below=forms.get_form(
                'Create Role',
                [
                    html_input.get_text_input("role"),
                    html_input.get_checkbox('permissions', [(action, False) for action in permissions])
                ],
                submit_name='create role',
                method='put',
                action='/auth/role'
            )
        )
        _roles = await server.auth_roles.select('*')

        return admin_table

    async def get_action_details(action: str):
        permission = await server.auth_actions.select(
            '*', where={'action': action}
        )
        permission = permission.copy()
        if not permission:
            raise HTTPException(
                status_code=404,
                detail=f"No permission with name {action} exists"
            )
        permission = permission[0]

        all_roles = await server.auth_roles.select('*')
        for role in all_roles.copy():
            if isinstance(role['permissions'], dict):
                role['permissions'] = role['permissions']['actions']
        
        roles = []
        for role in all_roles:
            if permission['action'] in role['permissions']:
                roles.append(role['role'])
                break
        
        all_groups = await server.auth_groups.select('group_name', 'roles')
        for group in all_groups.copy():
            if isinstance(group['roles'], dict):
                group['roles'] = group['roles']['roles']
        groups = []
        for group in all_groups:
            for role in group['roles']:
                if role in roles:
                    groups.append(group['group_name'])
                    break

        all_users = await server.auth_users.select('username', 'groups')
        users = []
        for user in all_users.copy():
            if isinstance(user['groups'], dict):
                user['groups'] = user['groups']['groups']
        for user in all_users:
            for group in user['groups']:
                if group in groups:
                    users.append(user['username'])
                    break
                
        update_form = forms.get_form(
            f'Update {action}',
            [
                html_input.get_text_input("action", value=action),
                html_input.get_text_input("details", value=permission['details'])
            ],
            submit_name='update permission',
            method='post',
            action='/auth/permissions'
        )

        modal_row = row.get_row(
            card.get_card(
                f'{action}',
                update_form,
                size=12
            )+
            card.get_card(
                f"Users",
                ''.join([
                    buttons.get_button(
                        user,
                        color='success', 
                        href=f'{admin_prefix}/user/{user}'
                    ) for user in users
                ]),
                size=4
            )+
            card.get_card(
                f"Groups",
                ''.join([
                    buttons.get_button(
                        group,
                        color='success', 
                        href=f'{admin_prefix}/group/{group}'
                    ) for group in groups
                ]),
                size=4
            )+
            card.get_card(
                f"Roles",
                ''.join([
                    buttons.get_button(
                        role,
                        color='success', 
                        href=f'{admin_prefix}/role/{role}'
                    ) for role in roles
                ]),
                size=4
            )
        )
        return modal_row
    @admin_gui.get('/action/{action}', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_action_page(action: str, access_token=None):
        permission = await server.auth_actions.select(
            '*', where={'action': action}
        )
        if not permission:
            raise HTTPException(
                status_code=404,
                detail=f"No permission with name {action} exists"
            )
        action_page = admin.get_admin_page(
            name=action, 
            sidebar=server.admin.sidebar,
            body=await get_action_details(action),
            current_user=access_token['permissions']['users'][0],
            modals=logout_modal
        )
        return action_page

    @admin_gui.get('/actions', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_actions(access_token=None):
        permissions = await server.auth_actions.select('*')
        modals = [logout_modal]
        for permission in permissions:
            action = permission['action']
            modals.append(modal.get_modal(
                    f'delete{action}Modal',
                    alert='',
                    body=forms.get_form(
                        f'Delete Action {action}',
                        [
                            buttons.get_button(
                                'Go Back',
                                color='success', 
                                href=f'{admin_prefix}/actions'
                        )],
                        submit_name='delete action',
                        method='delete',
                        action=f'/auth/permission?action={action}'
                    ),
                    footer='',
                    size='sm'
                )
            )
            modals.append(modal.get_modal(
                f'view_{action}',
                alert='',
                body=await get_action_details(action),
                footer='',
                size='lg'
            ))
            actions = ( 
                buttons.get_split_button(
                    f'view / edit',
                    icon='eye',
                    modal=f'view_{action}'
                ) + 
                buttons.get_split_button(
                    f'delete', 
                    modal=f'delete{action}Modal', 
                    color='danger',
                    icon='trash'
                )
            )
            permission[' '] = actions
        return server.admin.table_page(
            'Permissions',
            permissions if len(permissions) > 0 else [{'action': 'NO_ACTIONS', 'details': ''}],
            current_user=access_token['permissions']['users'][0],
            modals=''.join(modals),
            above="",
            below=forms.get_form(
                'Create Permission',
                [
                    html_input.get_text_input("action"),
                    html_input.get_text_input("details"),
                ],
                submit_name='create permission',
                method='put',
                action='/auth/permissions'
            )
        )
    

    def get_token_details(token: dict):
        users = token['users']
        groups = token['groups']
        roles = token['roles']
        actions = token['actions']

        modal_row = card.get_card(
            f"{users[0]} Token Permissions",
            body = row.get_row(
                card.get_card(
                    f"Users",
                    ''.join([
                        buttons.get_button(
                            user,
                            color='success', 
                            href=f'{admin_prefix}/user/{user}'
                        ) for user in users
                    ]),
                    size=4
                )+
                card.get_card(
                    f"Groups",
                    ''.join([
                        buttons.get_button(
                            group,
                            color='success', 
                            href=f'{admin_prefix}/group/{group}'
                        ) for group in groups
                    ]),
                    size=4
                )+
                card.get_card(
                    f"Roles",
                    ''.join([
                        buttons.get_button(
                            role,
                            color='success', 
                            href=f'{admin_prefix}/role/{role}'
                        ) for role in roles
                    ]),
                    size=4
                )+
                card.get_card(
                    f"Actions",
                    ''.join([
                        buttons.get_button(
                            action,
                            color='success', 
                            href=f'{admin_prefix}/action/{action}'
                        ) for action in actions
                    ]),
                    size=4
                )
            ),
            size=12
        )
        return modal_row
    
    @admin_gui.get('/tokens', response_class=HTMLResponse, send_token=True, include_in_schema=False)
    async def admin_tokens(access_token=None):
        tokens_raw = await server.auth_tokens.select('*')
        DO_NOT_DISPLAY = {'token_id', 'token'}

        tokens = []
        for ind, token in enumerate(tokens_raw):
            tk = {'number': ind}
            for k,v in token.items():
                if k in DO_NOT_DISPLAY:
                    continue
                tk[k] = v
            tokens.append(tk)
                
    
        modals = [logout_modal]
        token_index = {}
        for token in tokens:
            token_number = token['number']
            token_id = tokens_raw[token_number]['token_id']
            token_user = token['username']
            modals.append(modal.get_modal(
                    f'revoke{token_number}Modal',
                    alert='',
                    body=forms.get_form(
                        f"Revoke Token {token_number} for {token_user}",
                        [
                            buttons.get_button(
                                'Go Back',
                                color='success', 
                                href=f'{admin_prefix}/tokens'
                        )],
                        submit_name='revoke token',
                        method='delete',
                        action=f'/auth/token?token_id={token_id}'
                    ),
                    footer='',
                    size='sm'
                )
            )
            token_details = tokens_raw[token_number]['token']
            modals.append(modal.get_modal(
                f'view_{token_number}',
                alert='',
                body=get_token_details(token_details),
                footer='',
                size='lg'
            ))
            actions = ( 
                buttons.get_split_button(
                    f'view',
                    icon='eye',
                    modal=f'view_{token_number}'
                ) + 
                buttons.get_split_button(
                    f'revoke', 
                    modal=f'revoke{token_number}Modal', 
                    color='danger',
                    icon='trash'
                )
            )
            token[' '] = actions
        return server.admin.table_page(
            'Tokens',
            tokens if len(tokens) > 0 else [
                {
                    'username': 'NO USER ISSUED TOKENS', 
                    'issued': '',
                    'expiration': ''
                }
            ],
            current_user=access_token['permissions']['users'][0],
            modals=''.join(modals),
            above="",
            below=''
        )

    
    @server.server.get('/login', response_class=HTMLResponse, tags=['Login'])
    async def admin_login():
        return server.admin.login_page(welcome_message='Login to begin')