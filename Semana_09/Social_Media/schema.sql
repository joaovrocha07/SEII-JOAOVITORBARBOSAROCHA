drop table if exists posts;
	create table posts (
		id integrer primary key autoincrement,
		name text not null,
		content text not null
);