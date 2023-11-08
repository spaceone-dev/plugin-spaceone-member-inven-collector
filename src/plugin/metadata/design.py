DESIGN_MEMBER_METADATA = {
    'view': {
        'search': [
            {
                'key': 'data.id',
                'name': 'Member ID'
            },
            {
                'key': 'data.part',
                'name': 'Part',
            },
            {
                'key': 'data.email',
                'name': 'Email'
            },
            {
                'key': 'data.join_date',
                'name': 'Join Date'
            }
        ],
        'table': {
            'layout': {
                'name': '',
                'type': 'query-search-table',
                'options': {
                    'default_sort': {
                        'key': 'data.id',
                        'desc': False
                    },
                    'fields': [
                        {
                            'type': 'text',
                            'key': 'data.id',
                            'name': 'Member ID'
                        },
                        {
                            'type': 'text',
                            'key': 'data.part',
                            'name': 'Part',
                        },
                        {
                            'key': 'data.state',
                            'name': 'State',
                            'type': 'state',
                            'options': {
                                'icon': {
                                    'image': 'ic_sorting-descending',
                                }
                            }
                        },
                        {
                            'type': 'text',
                            'key': 'data.email',
                            'name': 'Email',
                        },
                        {
                            'type': 'text',
                            'key': 'data.join_date',
                            'name': 'Join Date',
                        }
                    ]
                }
            }
        },
        'widget': [

        ],
        "sub_data": {
            "layouts": [
                {
                    "name": "Details",
                    "type": "list",
                    "options": {
                        "layouts": [
                            {
                                "options": {
                                    "fields": [
                                        {
                                            'key': 'data.id',
                                            'name': 'Member ID'
                                        },
                                        {
                                            'key': 'data.part',
                                            'name': 'Part',
                                        },
                                        {
                                            'key': 'data.state',
                                            'name': 'State',
                                            'type': 'state',
                                            'options': {
                                                'text_color': 'blue',
                                                'icon': {
                                                    'image': 'fa-address-book'
                                                }
                                            }
                                        }
                                    ]
                                },
                                "name": "Division",
                                "type": "item"
                            },
                            {
                                "options": {
                                    "fields": [
                                        {
                                            'key': 'data.email',
                                            'name': 'Email'
                                        },
                                        {
                                            'key': 'data.join_date',
                                            'name': 'Join Date'
                                        }
                                    ]
                                },
                                "name": "Private",
                                "type": "item"
                            }
                        ]
                    }
                }
            ]
        }
    }
}