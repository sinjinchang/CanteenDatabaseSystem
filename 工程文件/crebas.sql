/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     10/19/2021 4:33:23 PM                        */
/*==============================================================*/


drop table if exists canteen;

drop table if exists food;

drop table if exists foodstyle;

drop table if exists mark;

drop table if exists `order`;

drop table if exists staff;

drop table if exists store;

drop table if exists userinfo;

/*==============================================================*/
/* Table: canteen                                               */
/*==============================================================*/
create table canteen
(
   canteen_id           smallint not null,
   canteen_name         char(64) not null,
   primary key (canteen_id)
);

/*==============================================================*/
/* Table: food                                                  */
/*==============================================================*/
create table food
(
   food_id              smallint not null,
   sto_store_id         smallint,
   foo_foodstyle_id     smallint,
   foodstyle_id         smallint not null,
   food_name            char(128) not null,
   food_price           smallint not null,
   store_id             smallint not null,
   primary key (food_id)
);

/*==============================================================*/
/* Table: foodstyle                                             */
/*==============================================================*/
create table foodstyle
(
   foodstyle_id         smallint not null,
   foodstyle_name       char(128) not null,
   primary key (foodstyle_id)
);

/*==============================================================*/
/* Table: mark                                                  */
/*==============================================================*/
create table mark
(
   comment_id           smallint not null,
   ord_order_id         smallint,
   sto_store_id         smallint,
   user_id              smallint,
   comment_score        smallint not null,
   comment_content      char(128) not null,
   order_id             smallint not null,
   store_id             smallint not null,
   primary key (comment_id)
);

/*==============================================================*/
/* Table: "order"                                               */
/*==============================================================*/
create table `order`
(
   order_id             smallint not null,
    user_id              smallint not null,
   store_id             smallint not null, 
   order_time           date not null,
    food_id              smallint not null,
   comment_id           smallint,
   primary key (order_id)
);

/*==============================================================*/
/* Table: staff                                                 */
/*==============================================================*/
create table staff
(
   staff_id             smallint not null,
   sto_store_id         smallint,
   staff_name           char(128) not null,
   staff_age            smallint not null,
   store_id             smallint not null,
   primary key (staff_id)
);

/*==============================================================*/
/* Table: store                                                 */
/*==============================================================*/
create table store
(
   store_id             smallint not null,
   can_canteen_id       smallint,
   store_name           char(128) not null,
   store_location       char(128) not null,
   canteen_id           smallint not null,
   store_opentime       time not null,
   primary key (store_id)
);

/*==============================================================*/
/* Table: userinfo                                              */
/*==============================================================*/
create table userinfo
(
   user_id              smallint not null,
   user_name            char(128) not null,
   user_password        char(64) not null,
   primary key (user_id)
);

alter table food add constraint FK_Relationship_7 foreign key (sto_store_id)
      references store (store_id) on delete restrict on update restrict;

alter table food add constraint FK_food_foodstyle foreign key (foo_foodstyle_id)
      references foodstyle (foodstyle_id) on delete restrict on update restrict;

alter table mark add constraint FK_Relationship_3 foreign key (sto_store_id)
      references store (store_id) on delete restrict on update restrict;

alter table mark add constraint FK_Relationship_4 foreign key (user_id)
      references userinfo (user_id) on delete restrict on update restrict;

alter table mark add constraint FK_Relationship_5 foreign key (ord_order_id)
      references `order` (order_id) on delete restrict on update restrict;

alter table `order` add constraint FK_Relationship_6 foreign key (comment_id)
      references mark (comment_id) on delete restrict on update restrict;

alter table `order` add constraint FK_Relationship_8 foreign key (user_id)
      references userinfo (user_id) on delete restrict on update restrict;

alter table staff add constraint FK_Relationship_9 foreign key (sto_store_id)
      references store (store_id) on delete restrict on update restrict;

alter table store add constraint FK_Relationship_2 foreign key (can_canteen_id)
      references canteen (canteen_id) on delete restrict on update restrict;

