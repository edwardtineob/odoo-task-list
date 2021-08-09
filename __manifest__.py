{
    'name': 'To-Do Application',
    'description': 'Tutorial To Do App Module for Odoo',
    'author': 'Edward Tineo',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml'
    ]
}