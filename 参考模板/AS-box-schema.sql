CREATE TABLE `erp_order`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `internal_order_number` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '内部订单号',
  `online_order_number` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '线上订单号',
  `store_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '店铺名称',
  `full_channel_user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '全渠道用户ID',
  `shipping_date` datetime NULL DEFAULT NULL COMMENT '发货日期',
  `payment_date` datetime NULL DEFAULT NULL COMMENT '付款日期',
  `payable_amount` decimal(10, 2) NULL DEFAULT NULL COMMENT '应付金额',
  `paid_amount` decimal(10, 2) NULL DEFAULT NULL COMMENT '已付金额',
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '状态',
  `consignee` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '收货人',
  `spu` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '款号',
  `order_time` datetime NULL DEFAULT NULL COMMENT '下单时间',
  `province` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '省份',
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '城市',
  `platform` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '平台站点',
  `sub_order_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '子订单编号',
  `online_sub_order_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '线上子订单编号',
  `original_online_order_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '原始线上订单号',
  `sku` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品编码',
  `quantity` int NULL DEFAULT NULL COMMENT '数量',
  `unit_price` decimal(10, 2) NULL DEFAULT NULL COMMENT '商品单价',
  `product_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品名称',
  `color_and_spec` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '颜色及规格',
  `product_amount` decimal(10, 2) NULL DEFAULT NULL COMMENT '商品金额',
  `original_price` decimal(10, 2) NULL DEFAULT NULL COMMENT '原价',
  `is_gift` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '是否赠品',
  `sub_order_status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '子订单状态',
  `refund_status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '退款状态',
  `registered_quantity` int NULL DEFAULT NULL COMMENT '登记数量',
  `actual_refund_quantity` int NULL DEFAULT NULL COMMENT '实退数量',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_erp_order_spu`(`spu` ASC) USING BTREE,
  INDEX `idx_erp_order_sku`(`sku` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20423 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '聚水潭订单数据表' ROW_FORMAT = Dynamic;

CREATE TABLE `new_sku_sales`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `statistics_date` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '统计日期',
  `shop_name` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '店铺名称',
  `product_id` bigint NULL DEFAULT NULL COMMENT '商品ID',
  `product_name` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品名称',
  `sku_id` bigint NULL DEFAULT NULL COMMENT 'SKU ID',
  `sku_name` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'SKU名称',
  `cart_add_count` int NULL DEFAULT NULL COMMENT '加购件数',
  `order_count` int NULL DEFAULT NULL COMMENT '下单件数',
  `order_buyer_count` int NULL DEFAULT NULL COMMENT '下单买家数',
  `order_amount` int NULL DEFAULT NULL COMMENT '下单金额',
  `payment_count` int NULL DEFAULT NULL COMMENT '支付件数',
  `payment_buyer_count` int NULL DEFAULT NULL COMMENT '支付买家数',
  `payment_amount` int NULL DEFAULT NULL COMMENT '支付金额',
  `style_number` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '款号',
  `color` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '颜色',
  `sub_style_number` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '分款号',
  `wave_band` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '波段',
  `link` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '链接',
  `online_three` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '上线前三天',
  `record_date` datetime NULL DEFAULT NULL COMMENT '记录日期',
  `sku` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品编码',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_new_sku_sales_product_id`(`product_id` ASC) USING BTREE,
  INDEX `idx_new_sku_sales_sku`(`sku` ASC) USING BTREE,
  INDEX `idx_new_sku_sales_statistics_date`(`record_date` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21589 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '新品SKU销售原始表' ROW_FORMAT = Dynamic;

CREATE TABLE `sku_data_base`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `SPU` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '款式编码',
  `SKU` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品编码',
  `product_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品名称',
  `color_specification` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '颜色及规格',
  `color` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '颜色',
  `Specification` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '规格',
  `basic_price` int NULL DEFAULT NULL COMMENT '基本售价',
  `tag_price` int NULL DEFAULT NULL COMMENT '市场吊牌价',
  `Classification` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '分类',
  `product_label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品标签',
  `product_attributes` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品属性',
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `season` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '季节',
  `fabric_component` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '面料成份',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_sku_data_base_spu`(`SPU` ASC) USING BTREE,
  INDEX `idx_sku_data_base_sku`(`SKU` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24466 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '商品基础资料表' ROW_FORMAT = Dynamic;

CREATE TABLE `spu_manages_feishu`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `spu` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '款号',
  `style_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '款式名称商品名称',
  `product_tags` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品标签',
  `product_category` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '产品分类',
  `return_rate` decimal(5, 4) NULL DEFAULT NULL COMMENT '退货率',
  `sales_quantity` int NULL DEFAULT NULL COMMENT '销售数量',
  `net_sales` int NULL DEFAULT NULL COMMENT '净销量',
  `shipped_sales` int NULL DEFAULT NULL COMMENT '实发数量',
  `shipped_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '实发金额',
  `sales_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '销售金额',
  `sales_cost` decimal(12, 2) NULL DEFAULT NULL COMMENT '销售成本',
  `shipped_cost` decimal(12, 2) NULL DEFAULT NULL COMMENT '实发成本',
  `gross_profit` decimal(12, 2) NULL DEFAULT NULL COMMENT '销售毛利',
  `return_quantity` int NULL DEFAULT NULL COMMENT '退货数量',
  `actual_return_quantity` int NULL DEFAULT NULL COMMENT '实退数量',
  `return_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '退货金额',
  `return_cost` decimal(12, 2) NULL DEFAULT NULL COMMENT '退货成本',
  `actual_return_cost` decimal(12, 2) NULL DEFAULT NULL COMMENT '实退成本',
  `actual_return_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '实退金额',
  `return_gross_profit` decimal(12, 3) NULL DEFAULT NULL COMMENT '退货毛利',
  `net_sales_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '净销售额',
  `net_sales_cost` decimal(12, 2) NULL DEFAULT NULL COMMENT '净销售成本',
  `net_sales_profit` decimal(12, 2) NULL DEFAULT NULL COMMENT '净销售毛利',
  `discount_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '优惠金额',
  `shipping_income` decimal(12, 2) NULL DEFAULT NULL COMMENT '运费收入',
  `shipping_cost` decimal(12, 2) NULL DEFAULT NULL COMMENT '运费支出',
  `base_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '基本金额',
  `paid_amount` decimal(12, 2) NULL DEFAULT NULL COMMENT '已付金额',
  `shipped_return_rate` decimal(5, 4) NULL DEFAULT NULL COMMENT '实发退货率',
  `base_price` decimal(12, 2) NULL DEFAULT NULL COMMENT '基本售价',
  `five_category_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '五类',
  `continuation_note` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '延续内容',
  `continuation_month` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '延续月份',
  `year` int NULL DEFAULT NULL COMMENT '年份',
  `season` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '季节',
  `product_status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品状态',
  `discount` decimal(3, 2) NULL DEFAULT NULL COMMENT '折扣',
  `stock_on_hand` int NULL DEFAULT NULL COMMENT '现货',
  `inventory_quantity` int NULL DEFAULT NULL COMMENT '货量',
  `main_warehouse` int NULL DEFAULT NULL COMMENT '主仓',
  `skc_inventory` int NULL DEFAULT NULL COMMENT 'SKC库存',
  `middle_category` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '中类',
  `net_sales_revenue` decimal(10, 2) NULL DEFAULT NULL COMMENT '净销售金额',
  `designer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '设计师(人员)',
  `element_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '元素类型',
  `launch_batch` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '上新波次',
  `sales_peak` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '销售顶峰',
  `sales_cycle` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '可售周期',
  `small_wave` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '小波段',
  `super_live` int NULL DEFAULT NULL COMMENT '超级直播',
  `continu_direction` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '延续方向',
  `continu_result` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '延续结果',
  `review_conclusions` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '复盘结论',
  `sale_rating` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '开售评级',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2513 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '飞书商品经营数据表' ROW_FORMAT = Dynamic;

CREATE TABLE `user_unique_compare`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '全渠道用户ID',
  `user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户昵称',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_user_unique_compare_user_id`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '全渠道表' ROW_FORMAT = Dynamic;

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `after0331_skc_data_base_view` AS select distinct `s`.`id` AS `id`,`s`.`SKU` AS `sku`,`s`.`SPU` AS `spu`,(case when ((`s`.`SKU` is null) or (`s`.`SKU` = '')) then NULL when (right(`s`.`SKU`,4) = 'XXXL') then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 4)) when (right(`s`.`SKU`,3) in ('XXL','XLC','XSC','XSD','XLD')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 3)) when (right(`s`.`SKU`,2) in ('XS','XL','LC','MC','SC','MD','SD','LD','L1','M1','S1','L2','M2','S2','均码','')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 2)) when (right(`s`.`SKU`,1) in ('X','L','S','M','F')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 1)) else NULL end) AS `skc`,`s`.`color` AS `color`,(case when (`s`.`Specification` is null) then NULL else replace(replace(replace(replace(`s`.`Specification`,'加长','C'),'2X','XX'),'3X','XXX'),'4X','XXXX') end) AS `specification`,`s`.`basic_price` AS `basic_price`,`s`.`tag_price` AS `tag_price`,`s`.`Classification` AS `classification`,`s`.`fabric_component` AS `fabric_component`,`f`.`five_category_type` AS `five_category_type`,`f`.`season` AS `season`,`s`.`create_time` AS `create_time`,`s`.`product_attributes` AS `product_attributes`,`f`.`middle_category` AS `middle_category`,`f`.`year` AS `year`,concat(`f`.`year`,`f`.`season`) AS `season_year` from (`sku_data_base` `s` left join `spu_manages_feishu` `f` on((`s`.`SPU` = `f`.`spu`))) where ((`s`.`product_attributes` <> '原材料') and (`s`.`create_time` > '2025-03-31 23:59:59'));

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `after0331_skc_score_view` AS select distinct `d`.`skc` AS `skc`,`d`.`spu` AS `spu`,`s`.`Exposure_to_skin` AS `Exposure_to_skin`,`s`.`Curve` AS `Curve`,`s`.`Texture_refinement` AS `Texture_refinement`,`s`.`Decorative_splendor_is_magnificent` AS `Decorative_splendor_is_magnificent`,`s`.`Fit` AS `Fit`,`s`.`Color_splendidness` AS `Color_splendidness`,`s`.`Structural_complexity` AS `Structural_complexity`,`s`.`Exposure_to_skin_Desc` AS `Exposure_to_skin_Desc`,`s`.`Curve_Desc` AS `Curve_Desc`,`s`.`Texture_refinement_Desc` AS `Texture_refinement_Desc`,`s`.`Decorative_splendor_is_magnificent_Desc` AS `Decorative_splendor_is_magnificent_Desc`,`s`.`Fit_Desc` AS `Fit_Desc`,`s`.`Color_splendidness_Desc` AS `Color_splendidness_Desc`,`s`.`Structural_complexity_Desc` AS `Structural_complexity_Desc` from (`after0331_skc_data_base_view` `d` left join `skc_score_view` `s` on((`d`.`skc` = `s`.`skc`)));

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `before0331_skc_data_base_view` AS select distinct `s`.`id` AS `id`,`s`.`SKU` AS `sku`,`s`.`SPU` AS `spu`,(case when ((`s`.`SKU` is null) or (`s`.`SKU` = '')) then NULL when (right(`s`.`SKU`,4) = 'XXXL') then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 4)) when (right(`s`.`SKU`,3) in ('XXL','XLC','XSC','XSD','XLD')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 3)) when (right(`s`.`SKU`,2) in ('XS','XL','LC','MC','SC','MD','SD','LD','L1','M1','S1','L2','M2','S2','均码','')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 2)) when (right(`s`.`SKU`,1) in ('X','L','S','M','F')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 1)) else NULL end) AS `skc`,`s`.`color` AS `color`,(case when (`s`.`Specification` is null) then NULL else replace(replace(replace(replace(`s`.`Specification`,'加长','C'),'2X','XX'),'3X','XXX'),'4X','XXXX') end) AS `specification`,`s`.`basic_price` AS `basic_price`,`s`.`tag_price` AS `tag_price`,`s`.`Classification` AS `classification`,`s`.`fabric_component` AS `fabric_component`,`f`.`five_category_type` AS `five_category_type`,`f`.`season` AS `season`,`s`.`create_time` AS `create_time`,`s`.`product_attributes` AS `product_attributes`,`f`.`middle_category` AS `middle_category`,`f`.`year` AS `year`,concat(`f`.`year`,`f`.`season`) AS `season_year` from (`sku_data_base` `s` left join `spu_manages_feishu` `f` on((`s`.`SPU` = `f`.`spu`))) where ((`s`.`product_attributes` <> '原材料') and (`s`.`create_time` < '2025-03-31 23:59:59'));

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `before0331_skc_score_view` AS select distinct `d`.`skc` AS `skc`,`d`.`spu` AS `spu`,`s`.`Exposure_to_skin` AS `Exposure_to_skin`,`s`.`Curve` AS `Curve`,`s`.`Texture_refinement` AS `Texture_refinement`,`s`.`Decorative_splendor_is_magnificent` AS `Decorative_splendor_is_magnificent`,`s`.`Fit` AS `Fit`,`s`.`Color_splendidness` AS `Color_splendidness`,`s`.`Structural_complexity` AS `Structural_complexity`,`s`.`Exposure_to_skin_Desc` AS `Exposure_to_skin_Desc`,`s`.`Curve_Desc` AS `Curve_Desc`,`s`.`Texture_refinement_Desc` AS `Texture_refinement_Desc`,`s`.`Decorative_splendor_is_magnificent_Desc` AS `Decorative_splendor_is_magnificent_Desc`,`s`.`Fit_Desc` AS `Fit_Desc`,`s`.`Color_splendidness_Desc` AS `Color_splendidness_Desc`,`s`.`Structural_complexity_Desc` AS `Structural_complexity_Desc` from (`before0331_skc_data_base_view` `d` left join `skc_score_view` `s` on((`d`.`skc` = `s`.`skc`)));

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `erp_order_view` AS select distinct `erp_order`.`id` AS `id`,`erp_order`.`store_name` AS `store_name`,`erp_order`.`full_channel_user_id` AS `full_channel_user_id`,`erp_order`.`shipping_date` AS `shipping_date`,`erp_order`.`payment_date` AS `payment_date`,`erp_order`.`payable_amount` AS `payable_amount`,`erp_order`.`paid_amount` AS `paid_amount`,`erp_order`.`consignee` AS `consignee`,`erp_order`.`spu` AS `spu`,`erp_order`.`order_time` AS `order_time`,`erp_order`.`province` AS `province`,`erp_order`.`city` AS `city`,`erp_order`.`platform` AS `platform`,`erp_order`.`original_online_order_number` AS `original_online_order_number`,`erp_order`.`sku` AS `sku`,`erp_order`.`quantity` AS `quantity`,`erp_order`.`unit_price` AS `unit_price`,`erp_order`.`product_name` AS `product_name`,`erp_order`.`color_and_spec` AS `color_and_spec`,`erp_order`.`product_amount` AS `product_amount`,`erp_order`.`original_price` AS `original_price`,`erp_order`.`is_gift` AS `is_gift`,`erp_order`.`refund_status` AS `refund_status` from `erp_order` where ((`erp_order`.`refund_status` <> '退款关闭') and ((`erp_order`.`refund_status` <> '未申请退款') or (`erp_order`.`shipping_date` is not null)) and (`erp_order`.`unit_price` > 1));

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `five_category_group_a7399d6e1c1eddbe85a56bde8fcf3b69` AS select row_number() OVER (ORDER BY coalesce(`sdbv`.`five_category_type`,'未分组') )  AS `id`,`pv`.`full_channel_user_id` AS `full_channel_user_id`,coalesce(`sdbv`.`five_category_type`,'未分组') AS `five_category_type`,count(0) AS `sales_amount`,group_concat(distinct (case when (`sdbv`.`sku` is null) then (case when ((`pv`.`sku` is null) or (trim(`pv`.`sku`) = '')) then NULL when (right(upper(trim(`pv`.`sku`)),4) = 'XXXL') then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 4)) when (right(upper(trim(`pv`.`sku`)),3) in ('XLC','XSC','XSD','XLD','XXL')) then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 3)) when (right(upper(trim(`pv`.`sku`)),2) in ('XS','XL','LC','MC','SC','MD','SD','LD')) then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 2)) when (right(upper(trim(`pv`.`sku`)),1) in ('X','L','S','M','F')) then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 1)) else upper(trim(`pv`.`sku`)) end) else `sdbv`.`skc` end) order by (case when (`sdbv`.`sku` is null) then (case when ((`pv`.`sku` is null) or (trim(`pv`.`sku`) = '')) then NULL when (right(upper(trim(`pv`.`sku`)),4) = 'XXXL') then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 4)) when (right(upper(trim(`pv`.`sku`)),3) in ('XLC','XSC','XSD','XLD','XXL')) then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 3)) when (right(upper(trim(`pv`.`sku`)),2) in ('XS','XL','LC','MC','SC','MD','SD','LD')) then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 2)) when (right(upper(trim(`pv`.`sku`)),1) in ('X','L','S','M','F')) then left(upper(trim(`pv`.`sku`)),(char_length(trim(`pv`.`sku`)) - 1)) else upper(trim(`pv`.`sku`)) end) else `sdbv`.`skc` end) ASC separator '、') AS `skc_list` from (`positiv_view_a7399d6e1c1eddbe85a56bde8fcf3b69` `pv` left join `skc_data_base_view` `sdbv` on((`pv`.`sku` = `sdbv`.`sku`))) group by `pv`.`full_channel_user_id`,coalesce(`sdbv`.`five_category_type`,'未分组');

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `negative_view_a7399d6e1c1eddbe85a56bde8fcf3b69` AS select `erp_order_view`.`id` AS `id`,`erp_order_view`.`store_name` AS `store_name`,`erp_order_view`.`full_channel_user_id` AS `full_channel_user_id`,`erp_order_view`.`shipping_date` AS `shipping_date`,`erp_order_view`.`payment_date` AS `payment_date`,`erp_order_view`.`payable_amount` AS `payable_amount`,`erp_order_view`.`paid_amount` AS `paid_amount`,`erp_order_view`.`consignee` AS `consignee`,`erp_order_view`.`spu` AS `spu`,`erp_order_view`.`order_time` AS `order_time`,`erp_order_view`.`province` AS `province`,`erp_order_view`.`city` AS `city`,`erp_order_view`.`platform` AS `platform`,`erp_order_view`.`original_online_order_number` AS `original_online_order_number`,`erp_order_view`.`sku` AS `sku`,`erp_order_view`.`quantity` AS `quantity`,`erp_order_view`.`unit_price` AS `unit_price`,`erp_order_view`.`product_name` AS `product_name`,`erp_order_view`.`color_and_spec` AS `color_and_spec`,`erp_order_view`.`product_amount` AS `product_amount`,`erp_order_view`.`original_price` AS `original_price`,`erp_order_view`.`is_gift` AS `is_gift`,`erp_order_view`.`refund_status` AS `refund_status` from `erp_order_view` where ((`erp_order_view`.`refund_status` = '成功退款') and (`erp_order_view`.`full_channel_user_id` = 'a7399d6e1c1eddbe85a56bde8fcf3b69'));

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `positiv_view_225977a7ef98e2256a6cd0842aae0d99` AS select `erp_order_view`.`id` AS `id`,`erp_order_view`.`store_name` AS `store_name`,`erp_order_view`.`full_channel_user_id` AS `full_channel_user_id`,`erp_order_view`.`shipping_date` AS `shipping_date`,`erp_order_view`.`payment_date` AS `payment_date`,`erp_order_view`.`payable_amount` AS `payable_amount`,`erp_order_view`.`paid_amount` AS `paid_amount`,`erp_order_view`.`consignee` AS `consignee`,`erp_order_view`.`spu` AS `spu`,`erp_order_view`.`order_time` AS `order_time`,`erp_order_view`.`province` AS `province`,`erp_order_view`.`city` AS `city`,`erp_order_view`.`platform` AS `platform`,`erp_order_view`.`original_online_order_number` AS `original_online_order_number`,`erp_order_view`.`sku` AS `sku`,`erp_order_view`.`quantity` AS `quantity`,`erp_order_view`.`unit_price` AS `unit_price`,`erp_order_view`.`product_name` AS `product_name`,`erp_order_view`.`color_and_spec` AS `color_and_spec`,`erp_order_view`.`product_amount` AS `product_amount`,`erp_order_view`.`original_price` AS `original_price`,`erp_order_view`.`is_gift` AS `is_gift`,`erp_order_view`.`refund_status` AS `refund_status` from `erp_order_view` where ((`erp_order_view`.`refund_status` = '未申请退款') and (`erp_order_view`.`full_channel_user_id` = '225977a7ef98e2256a6cd0842aae0d99'));

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `skc_data_base_view` AS select distinct `s`.`id` AS `id`,`s`.`SKU` AS `sku`,`s`.`SPU` AS `spu`,(case when ((`s`.`SKU` is null) or (`s`.`SKU` = '')) then NULL when (right(`s`.`SKU`,4) = 'XXXL') then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 4)) when (right(`s`.`SKU`,3) in ('XXL','XLC','XSC','XSD','XLD')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 3)) when (right(`s`.`SKU`,2) in ('XS','XL','LC','MC','SC','MD','SD','LD','L1','M1','S1','L2','M2','S2','均码','')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 2)) when (right(`s`.`SKU`,1) in ('X','L','S','M','F')) then left(`s`.`SKU`,(char_length(`s`.`SKU`) - 1)) else NULL end) AS `skc`,`s`.`color` AS `color`,(case when (`s`.`Specification` is null) then NULL else replace(replace(replace(replace(`s`.`Specification`,'加长','C'),'2X','XX'),'3X','XXX'),'4X','XXXX') end) AS `specification`,`s`.`basic_price` AS `basic_price`,`s`.`tag_price` AS `tag_price`,`s`.`Classification` AS `classification`,`s`.`fabric_component` AS `fabric_component`,`f`.`five_category_type` AS `five_category_type`,`s`.`create_time` AS `create_time`,`f`.`season` AS `season`,`s`.`product_attributes` AS `product_attributes`,`f`.`middle_category` AS `middle_category`,`f`.`year` AS `year`,concat(`f`.`year`,`f`.`season`) AS `season_year` from (`sku_data_base` `s` left join `spu_manages_feishu` `f` on((`s`.`SPU` = `f`.`spu`))) where (`s`.`product_attributes` <> '原材料');

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `skc_score_base_qiu6_distinct` AS with `ranked_data` as (select `skc_score_base_qiu6`.`id` AS `id`,`skc_score_base_qiu6`.`sku` AS `sku`,`skc_score_base_qiu6`.`spu` AS `spu`,`skc_score_base_qiu6`.`skc` AS `skc`,`skc_score_base_qiu6`.`color` AS `color`,`skc_score_base_qiu6`.`specification` AS `specification`,`skc_score_base_qiu6`.`basic_price` AS `basic_price`,`skc_score_base_qiu6`.`tag_price` AS `tag_price`,`skc_score_base_qiu6`.`classification` AS `classification`,`skc_score_base_qiu6`.`fabric_component` AS `fabric_component`,`skc_score_base_qiu6`.`five_category_type` AS `five_category_type`,`skc_score_base_qiu6`.`create_time` AS `create_time`,`skc_score_base_qiu6`.`season` AS `season`,`skc_score_base_qiu6`.`product_attributes` AS `product_attributes`,`skc_score_base_qiu6`.`middle_category` AS `middle_category`,`skc_score_base_qiu6`.`year` AS `year`,`skc_score_base_qiu6`.`season_year` AS `season_year`,`skc_score_base_qiu6`.`Exposure_to_skin` AS `Exposure_to_skin`,`skc_score_base_qiu6`.`Curve` AS `Curve`,`skc_score_base_qiu6`.`Texture_refinement` AS `Texture_refinement`,`skc_score_base_qiu6`.`Decorative_splendor_is_magnificent` AS `Decorative_splendor_is_magnificent`,`skc_score_base_qiu6`.`Fit` AS `Fit`,`skc_score_base_qiu6`.`Color_splendidness` AS `Color_splendidness`,`skc_score_base_qiu6`.`Structural_complexity` AS `Structural_complexity`,`skc_score_base_qiu6`.`Exposure_to_skin_Desc` AS `Exposure_to_skin_Desc`,`skc_score_base_qiu6`.`Curve_Desc` AS `Curve_Desc`,`skc_score_base_qiu6`.`Texture_refinement_Desc` AS `Texture_refinement_Desc`,`skc_score_base_qiu6`.`Decorative_splendor_is_magnificent_Desc` AS `Decorative_splendor_is_magnificent_Desc`,`skc_score_base_qiu6`.`Fit_Desc` AS `Fit_Desc`,`skc_score_base_qiu6`.`Color_splendidness_Desc` AS `Color_splendidness_Desc`,`skc_score_base_qiu6`.`Structural_complexity_Desc` AS `Structural_complexity_Desc`,row_number() OVER (PARTITION BY `skc_score_base_qiu6`.`skc` ORDER BY `skc_score_base_qiu6`.`spu` )  AS `rn` from `skc_score_base_qiu6`) select `ranked_data`.`id` AS `id`,`ranked_data`.`sku` AS `sku`,`ranked_data`.`spu` AS `spu`,`ranked_data`.`skc` AS `skc`,`ranked_data`.`color` AS `color`,`ranked_data`.`specification` AS `specification`,`ranked_data`.`basic_price` AS `basic_price`,`ranked_data`.`tag_price` AS `tag_price`,`ranked_data`.`classification` AS `classification`,`ranked_data`.`fabric_component` AS `fabric_component`,`ranked_data`.`five_category_type` AS `five_category_type`,`ranked_data`.`create_time` AS `create_time`,`ranked_data`.`season` AS `season`,`ranked_data`.`product_attributes` AS `product_attributes`,`ranked_data`.`middle_category` AS `middle_category`,`ranked_data`.`year` AS `year`,`ranked_data`.`season_year` AS `season_year`,`ranked_data`.`Exposure_to_skin` AS `Exposure_to_skin`,`ranked_data`.`Curve` AS `Curve`,`ranked_data`.`Texture_refinement` AS `Texture_refinement`,`ranked_data`.`Decorative_splendor_is_magnificent` AS `Decorative_splendor_is_magnificent`,`ranked_data`.`Fit` AS `Fit`,`ranked_data`.`Color_splendidness` AS `Color_splendidness`,`ranked_data`.`Structural_complexity` AS `Structural_complexity`,`ranked_data`.`Exposure_to_skin_Desc` AS `Exposure_to_skin_Desc`,`ranked_data`.`Curve_Desc` AS `Curve_Desc`,`ranked_data`.`Texture_refinement_Desc` AS `Texture_refinement_Desc`,`ranked_data`.`Decorative_splendor_is_magnificent_Desc` AS `Decorative_splendor_is_magnificent_Desc`,`ranked_data`.`Fit_Desc` AS `Fit_Desc`,`ranked_data`.`Color_splendidness_Desc` AS `Color_splendidness_Desc`,`ranked_data`.`Structural_complexity_Desc` AS `Structural_complexity_Desc`,`ranked_data`.`rn` AS `rn` from `ranked_data` where (`ranked_data`.`rn` = 1);

CREATE ALGORITHM = UNDEFINED DEFINER = `annaspeak_root`@`%` SQL SECURITY DEFINER VIEW `skc_score_view` AS select distinct `annaspeak`.`erp_skc`.`SKC` AS `skc`,`annaspeak`.`erp_skc`.`SPU` AS `spu`,`annaspeak`.`erp_skc`.`Exposure_to_skin` AS `Exposure_to_skin`,`annaspeak`.`erp_skc`.`Curve` AS `Curve`,`annaspeak`.`erp_skc`.`Texture_refinement` AS `Texture_refinement`,`annaspeak`.`erp_skc`.`Decorative_splendor_is_magnificent` AS `Decorative_splendor_is_magnificent`,`annaspeak`.`erp_skc`.`Fit` AS `Fit`,`annaspeak`.`erp_skc`.`Color_splendidness` AS `Color_splendidness`,`annaspeak`.`erp_skc`.`Structural_complexity` AS `Structural_complexity`,`annaspeak`.`erp_skc`.`Exposure_to_skin_Desc` AS `Exposure_to_skin_Desc`,`annaspeak`.`erp_skc`.`Curve_Desc` AS `Curve_Desc`,`annaspeak`.`erp_skc`.`Texture_refinement_Desc` AS `Texture_refinement_Desc`,`annaspeak`.`erp_skc`.`Decorative_splendor_is_magnificent_Desc` AS `Decorative_splendor_is_magnificent_Desc`,`annaspeak`.`erp_skc`.`Fit_Desc` AS `Fit_Desc`,`annaspeak`.`erp_skc`.`Color_splendidness_Desc` AS `Color_splendidness_Desc`,`annaspeak`.`erp_skc`.`Structural_complexity_Desc` AS `Structural_complexity_Desc` from `annaspeak`.`erp_skc`;

