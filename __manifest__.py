# -*- coding: utf-8 -*-
{
    'name': "STUDENTS DETAILS RECORD",

    'summary': """ For managing student details""",

    'description': """
        The given module store details of students
    """,

    'author': "ults",
    'website': "https://www.ults.in/",


    'category': 'category',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/cron.xml',
        'wizard/createstudent.xml',
        'wizard/studentact.xml',
        'wizard/wiz.xml',
        'views/teachersview.xml',
        'views/showstudentdata.xml',
        'views/menu2.xml',
        'views/subjectview.xml',
        'views/st.xml',
        'views/sg.xml',
        'report/report.xml',
        'report/teacher_card.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
