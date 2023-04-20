'''
create table ParentTable (
    ParentId              number(9) not null,
    Description           varchar2(60) not null,
    constraint ParentTable_pk primary key (ParentId)
);

'''
'''
create table ChildTable (
    ChildId               number(9) not null,
    ParentId              number(9) not null,
    Description           varchar2(60) not null,
    constraint ChildTable_pk primary key (ChildId),
    constraint ChildTable_fk foreign key (ParentId)
            references ParentTable
);
'''


data = [
    (10, 'Parent 10'),
    (20, 'Parent 20'),
    (30, 'Parent 30'),
    (40, 'Parent 40'),
    (50, 'Parent 50')
]
cursor.executemany("insert into ParentTable values (:1, :2)", data)














