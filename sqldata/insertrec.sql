create database murthy;
use murthy;
create table invest_data(name VARCHAR(50),value FLOAT,quantity INTEGER,target FLOAT,tag VARCHAR(50));
insert into invest_data values('test','20.0',4,22,'short');
insert into invest_data values('test2','220.0',24,322,'long');
create table history_data(SYMBOL VARCHAR(20),SERIES VARCHAR(10),OPEN FLOAT,HIGH FLOAT,LOW FLOAT,CLOSE FLOAT,LAST FLOAT,PREVCLOSE FLOAT,TOTTRDQTY FLOAT,TOTTRDVAL FLOAT,TIMESTAMP varchar(20),TOTALTRADES FLOAT,col1 varchar(20), col2 varchar(20));
create table notes(note varchar(100),note_date date,impact varchar(20),sector varchar(20));
create table targets(name varchar(20),qty int,target float,target_date date,recurrance varchar(20),tartget_type varchar(20),description varchar(50));
