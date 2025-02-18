data = {
    'Sales': {
        'North': {
            'Alice': 'Manager',
            'Bob': 'Sales Executive',
            'Eve': 'Sales Coordinator',
            'John': 'Account Manager'
        },
        'South': {
            'Charlie': 'Sales Executive',
            'Grace': 'Regional Sales Manager',
            'Mallory': 'Business Development Associate'
        },
        'West': {
            'Oscar': 'Sales Executive',
            'Peggy': 'Account Executive',
            'Victor': 'Territory Sales Manager'
        }
    },
    'Marketing': {
        'Digital': {
            'David': 'SEO Specialist',
            'Hannah': 'Content Strategist',
            'Irene': 'Social Media Manager'
        },
        'Offline': {
            'Eve': 'Event Coordinator',
            'Jake': 'Brand Manager',
            'Liam': 'Public Relations Specialist'
        },
        'Research': {
            'Mia': 'Market Research Analyst',
            'Noah': 'Customer Insights Manager'
        }
    },
    'IT': {
        'Infrastructure': {
            'Quinn': 'Network Engineer',
            'Riley': 'System Administrator',
            'Sam': 'Cloud Architect'
        },
        'Development': {
            'Tina': 'Software Engineer',
            'Uma': 'Backend Developer',
            'Walter': 'Full Stack Developer'
        }
    },
    'HR': {
        'Recruitment': {
            'Yara': 'Recruitment Specialist',
            'Zane': 'Talent Acquisition Manager',
            'Nina': 'HR Coordinator'
        },
        'Employee Relations': {
            'Oliver': 'Employee Relations Specialist',
            'Sophia': 'HR Business Partner'
        }
    },
    'Finance': {
        'Accounting': {
            'Xander': 'Accountant',
            'Yvette': 'Accounts Payable Specialist',
            'Zara': 'Financial Analyst'
        },
        'Audit': {
            'Luna': 'Internal Auditor',
            'Mason': 'Compliance Officer'
        }
    }
}

'''
write a program to display the below output:


Sales
-----
North
South
West


Marketing
--------
Digital
Offline
Research


IT
---
Infrasturcture
Development

HR
---
Recruitment
Employee Relations

'''
print(data.keys())

for key in data.keys():
    #print(data[key])
    print(key)
    print("-"*10)
    for subkey in data[key]:
        print(subkey)
    print("\n")
