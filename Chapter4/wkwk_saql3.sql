/*
3. sale_dataスキーマのpurchase, product, coupon_logを⽤い以下の項⽬を
ユーザごとに集計せよ。
集計期間︓2017年5⽉1⽇~5⽉31⽇（※左記期間中に⼀度も購⼊していないユーザの出⼒は不要）
集計項⽬︓クーポン使⽤を考慮しない購⼊⾦額、クーポン使⽤を考慮した購⼊⾦額、商品名が「婦⼈
雑誌」である商品の購⼊回数
*/

SELECT
purch.user_id
,sum(prod.price) as "クーポン未使用金額"
,sum( prod.price-c.disc_amount) as "クーポン使用金額"
,count(prod.name) as "婦人雑誌購入回数"
FROM
purchase purch
inner join
product prod
on purch.product_id = prod.id
inner join 
coupon_log c
on purch.user_id = c.user_id
and purch.purchase_id = c.purchase_id
and purch.product_id = c.product_id
where 
(purch.create_at >= '2017-05-01 00:00:00'
AND purch.create_at <= '2017-05-30 00:00:00')
and
prod.name like '%婦人雑誌%'
group by purch.user_id
order by 1 asc
limit 15
;













------ 婦人雑誌の購入回数が増える

SELECT
-- count(*)
sum(prod.price)
FROM
purchase purch
left join
product prod
on
purch.product_id = prod.id
where
(purch.create_at >= '2017-05-01 00:00:00'
AND purch.create_at <= '2017-05-30 00:00:00')
AND
prod.name like '%婦人雑誌%'
group by purch.user_id
having purch.user_id = 10002
;

select
 user_id
 from 
 purchase

  where 
  user_id = 10001
  AND
(create_at >= '2017-05-01 00:00:00'
AND create_at <= '2017-05-30 00:00:00')
group by user_id
  ;




--(3)
SELECT
purch.user_id
-- ,ifnull(sum(prod.price),0) as "クーポン未使用金額"
,sum(prod.price) as "クーポン未使用金額"
-- ,ifnull(sum(prod.price-ifnull(c.disc_amount,0)),0) as "クーポン使用金額"
,sum(prod.price-ifnull(c.disc_amount,0)) as "クーポン使用金額"
,count(case when prod.name like '%婦人雑誌%' then prod.name else 0 end) as "婦人雑誌購入回数"
FROM
purchase purch
inner join
--  期間内に一度も買い物していないユーザの出力は不要なため
product prod
on 
purch.product_id = prod.id
AND
purch.create_at
between
'2017-05-01 00:00:00'
AND 
'2017-05-30 00:00:00'
left outer join 
coupon_log c
on 
-- purch.user_id = c.user_id
-- and 
purch.purchase_id = c.purchase_id
-- and 
-- purch.product_id = c.product_id
-- WHERE
group by purch.user_id
order by 1 asc
limit 10
;

-----


SELECT
count(*)
FROM
purchase purch
inner join
product prod
on 
purch.product_id = prod.id
AND
purch.create_at
between
'2017-05-01 00:00:00'
AND 
'2017-05-30 00:00:00'
where 
prod.name like '%婦人雑誌%'
and 
purch.user_id = '10001'
group by purch.user_id;






--(3)
SELECT
purch.user_id
,sum(prod.price - ifnull(c.disc_amount,0)) as "クーポン使用金額"
,sum(prod.price) as "クーポン未使用金額"
,count(case when prod.name like '%婦人雑誌%' then prod.name else 0 end) as "婦人雑誌購入回数"
FROM
purchase purch
-- left outer JOIN
inner join
coupon_log c
-- とりあえずpurchとcouponを結ぶ
--  couponはクーポンのある商品しか表示しないので外部結合する
on purch.user_id = c.user_id
and purch.purchase_id = c.purchase_id
-- left outer JOIN
inner join
product prod
on 
purch.product_id = prod.id
and
purch.create_at
between
'2017-05-01 00:00:00'
AND 
'2017-05-30 00:00:00'
-- where 
-- prod.name like '%婦人雑誌%'
-- and
-- (purch.create_at >= '2017-05-01 00:00:00'
-- AND purch.create_at <= '2017-05-30 00:00:00')
group by purch.user_id
-- having purch.user_id = '10001'
order by 1
limit 30
;



-- samp

SELECT
t1.user_id as user_id1
, t2.user_id as user_id2
, t1.purchase_id as purchase_id1
, t2.purchase_id as purchase_id2
-- (他のカラムも同様に書く)
FROM
purchase as t1
INNER JOIN
coupon_log as t2
ON
t1.user_id = t2.user_id
LIMIT 200;



SELECT
*
from
-- purchase
-- product
coupon_log
limit 10;

