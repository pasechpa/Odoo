{
    'name': "SMS Framework",
    'version': "1.0.1",
    'author': "Sythil",
    'category': "Tools",
    'summary':'Allows you to send and receive smses from multiple gateways',
    'description':'Allows you to send and receive smses from multiple gateways',    
    'license':'LGPL-3',
    'data': [
        'views/sms_views.xml',
        'views/res_partner_views.xml',
        'views/sms_message_views.xml',
        'views/sms_template_views.xml',
        'views/sms_account_views.xml',
        'views/sms_number_views.xml',
        'views/sms_compose_views.xml',
        'views/ir_actions_server_views.xml',
        'data/ir.cron.csv',
        'data/res.country.csv',
    ],
    'demo': [],
    'depends': [],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}