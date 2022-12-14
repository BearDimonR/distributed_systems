db = db.getSiblingDB('linkedin');

db.createCollection('users');

db.users.insertMany([
 {
    _id : 1,
    login: 'gnickols0@xinhuanet.com',
    password: '4zynnh',
    resumes: [
        {
            _id : 1,
            summary: 'Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula.',
            hobbies: [
                {
                    name: 'Western Cordilleran Bunchberry',
                },
                {
                    name: 'Alpine Sandmat',
                },
                {
                    name: 'Biatora Lichen',
                },
                {
                    name: 'Aleutian Rim Lichen',
                },
            ],
            positions: [
                {
                    name: "Upgradable executive attitude",
                    company: {
                        name: "Vistra Energy Corp.",
                    },
                    city: {
                        _id: 1,
                        name: 'Wilfrido Loor Moreira',
                        code: 56,
                    },
                },
                {
                    name: "Visionary motivating access",
                    company: {
                        name: "Limelight Networks, Inc.",
                    },
                    city: {
                        _id: 2,
                        name: 'Touho',
                        code: 43,
                    },
                },
                {
                    name: "Organized exuding encryption",
                    company: {
                        name: "Scorpio Bulkers Inc.",
                    },
                    city: {
                        _id: 3,
                        name: 'Kuala Lumpu',
                        code: 27,
                    },
                },
                {
                    name: "Object-based multi-tasking initiative",
                    company: {
                        name: "Dreyfus High Yield Strategies Fund",
                    },
                    city: {
                        _id: 4,
                        name: 'Salinggara',
                        code: 38,
                    },
                },
            ],
        }
    ]
  },
  {
    _id : 2,
    login: 'imicklewright1@europa.eu',
    password: 'abm7oIBb',
    resumes: [
        {
            _id : 2,
            summary: 'Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit.',
            hobbies: [
                {
                    name: 'Alpine Sandmat',
                },
                {
                    name: 'Biatora Lichen',
                },
                {
                    name: 'Aleutian Rim Lichen',
                },
                {
                    name: 'Aleutian Rim Lichen',
                },
            ],
            positions: [
                {
                    name: "Upgradable executive attitude",
                    company: {
                        name: "Fuel Tech, Inc.",
                    },
                    city: {
                        _id: 1,
                        name: 'Wilfrido Loor Moreira',
                        code: 56,
                    },
                },
                {
                    name: "Visionary motivating access",
                    company: {
                        name: "Fuel Tech, Inc.",
                    },
                    city: {
                        _id: 3,
                        name: 'Kuala Lumpur',
                        code: 27,
                    },
                },
                {
                    name: "Organized exuding encryption",
                    company: {
                        name: "Vistra Energy Corp.",
                    },
                    city: {
                        _id: 3,
                        name: 'Kuala Lumpu',
                        code: 27,
                    },
                },
                {
                    name: "Object-based multi-tasking initiative",
                    company: {
                        name: "Vistra Energy Corp.",
                    },
                    city: {
                        _id: 3,
                        name: 'Kuala Lumpur',
                        code: 27,
                    },
                },
            ]
        }
    ]
  }
]);