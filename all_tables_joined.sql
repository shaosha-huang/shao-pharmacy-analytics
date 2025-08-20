select distinct
    -- orders
      o.order_id
    , o.customer_id
    , o.order_date
    , year(o.order_date) as order_year
    , month(o.order_date) as order_month
    , o.product_id
    , o.quantity
    , o.shipping_delay_days
    , o.customer_rating
    , o.shipping_date
    , o.delivered_date
    , o.refill
    , o.prescribing_doctor
    , o.order_status
    , o.payment_method
    , o.order_total
    -- customers
    , c.name as customer_name
    , timestampdiff(year, c.birth_date, curdate()) as age
    , c.gender
    , c.state
    , c.registration_date
    , c.subscription_type
    , c.subscription_status
    -- products
    , p.product_name
    , p.product_category
    , p.price_usd
    , p.cost_usd
    , p.prescription_required
    , p.manufacturer
    , p.stock_quantity
from orders o
    left join products p on p.product_id = o.product_id
    left join customers c on c.customer_id = o.customer_id
where o.order_date >= curdate() - interval 5 year
order by o.order_date desc;