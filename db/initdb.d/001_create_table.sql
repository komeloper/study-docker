-- デモ用テーブルを作成
CREATE TABLE `database`.demo_table (
  id BIGINT auto_increment NOT NULL COMMENT 'Primary Key',
  created_at DATETIME DEFAULT NULL COMMENT '作成日時',
  updated_at DATETIME DEFAULT NULL COMMENT '更新日時',
  value varchar(100) NULL COMMENT '値',
  CONSTRAINT demo_table_pk PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'demo_table';
