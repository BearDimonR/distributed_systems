:begin

CREATE
(`user1`:`user` {
	`login`: "gnickols0@xinhuanet.com",
	`password`: "4zynnh"
}),

(`user2`:`user` {
	`login`: "imicklewright1@europa.eu",
	`password`: "abm7oIBb"
}),

(`hobby1`:`hobby` {
	`name`: "Western Cordilleran Bunchberry"
}),

(`hobby2`:`hobby` {
	`name`: "Alpine Sandmat"
}),

(`hobby3`:`hobby` {
	`name`: "Biatora Lichen"
}),

(`hobby4`:`hobby` {
	`name`: "Biatora Lichen"
}),

(`hobby5`:`hobby` {
	`name`: "Aleutian Rim Lichen"
}),

(`resume1`:`resume` {
	`id`: 1,
	`summary`: "Praesent blandit lacinia er. Biatora Lichen"
}),

(`resume2`:`resume` {
	`id`: 2,
	`summary`: "Praesent blandit lacinia er. Bia. Aleutian Rim Lichen"
}),

(resume1)-[:HAS_HOBBY]->(hobby1),
(resume1)-[:HAS_HOBBY]->(hobby2),
(resume1)-[:HAS_HOBBY]->(hobby3),
(resume1)-[:HAS_HOBBY]->(hobby5),

(resume2)-[:HAS_HOBBY]->(hobby3),
(resume2)-[:HAS_HOBBY]->(hobby5),
(resume2)-[:HAS_HOBBY]->(hobby4),
(resume2)-[:HAS_HOBBY]->(hobby2),

(user1)-[:HAS_RESUME]->(resume1),
(user2)-[:HAS_RESUME]->(resume2),


(`city1`:`city` {
	`id`: 1,
	`name`: "Wilfrido Loor Moreira",
	`code`: 56
}),

(`city2`:`city` {
	`id`: 1,
	`name`: "Touho",
	`code`: 43
}),

(`city3`:`city` {
	`id`: 1,
	`name`: "Kuala Lumpur",
	`code`: 27
}),

(`city4`:`city` {
	`id`: 1,
	`name`: "Salinggara",
	`code`: 38
}),

(`city5`:`city` {
	`id`: 1,
	`name`: "Bukovany",
	`code`: 60
}),


(`company1`:`company` {
	`name`: "Vistra Energy Corp."
}),

(`company2`:`company` {
	`name`: "Limelight Networks, Inc."
}),

(`company3`:`company` {
	`name`: "Scorpio Bulkers Inc."
}),

(`company4`:`company` {
	`name`: "Dreyfus High Yield Strategies Fund"
}),

(`company5`:`company` {
	`name`: "Fuel Tech, Inc."
}),


(`position1`:`position` {
	`name`: "Upgradable executive attitude"
}),

(`position2`:`position` {
	`name`: "Visionary motivating access"
}),

(`position3`:`position` {
	`name`: "Organized exuding encryption"
}),

(`position4`:`position` {
	`name`: "Object-based multi-tasking initiative"
}),


(resume1)-[:HAS_POSITION]->(position1),
(resume1)-[:HAS_POSITION]->(position2),
(resume1)-[:HAS_POSITION]->(position3),
(resume1)-[:HAS_POSITION]->(position4),

(position1)-[:IN]->(city1),
(position2)-[:IN]->(city2),
(position3)-[:IN]->(city3),
(position4)-[:IN]->(city4),

(position1)-[:FOR]->(company1),
(position2)-[:FOR]->(company2),
(position3)-[:FOR]->(company3),
(position4)-[:FOR]->(company4),



(`position5`:`position` {
	`name`: "Profound object-oriented system engine"
}),

(`position6`:`position` {
	`name`: "Cross-platform zero defect utilisation"
}),

(`position7`:`position` {
	`name`: "Seamless zero administration core"
}),

(`position8`:`position` {
	`name`: "Inverse motivating budgetary management"
}),

(resume2)-[:HAS_POSITION]->(position5),
(resume2)-[:HAS_POSITION]->(position6),
(resume2)-[:HAS_POSITION]->(position7),
(resume2)-[:HAS_POSITION]->(position8),

(position5)-[:IN]->(city1),
(position6)-[:IN]->(city3),
(position7)-[:IN]->(city3),
(position8)-[:IN]->(city3),

(position5)-[:FOR]->(company5),
(position6)-[:FOR]->(company5),
(position7)-[:FOR]->(company1),
(position8)-[:FOR]->(company1)

:commit
