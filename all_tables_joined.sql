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
    , c.subs_change_id
    , c.name as customer_name
    , c.email
    , c.birth_date
    , timestampdiff(year, c.birth_date, curdate()) as age
    , c.gender
    , c.state
    , c.subscription_type
    , c.subscription_status
    , c.subs_change_date
    , c.auto_renewal
    -- products
    , p.product_id
    , p.product_name
    , p.product_category
    , p.price_usd
    , p.cost_usd
    , p.prescription_required
    , p.manufacturer
    , p.stock_quantity
    , p.description
    -- forecasts
    , f.forecast_id
    , f.year_month
    , f.product_id as forecast_product_id
    , f.actual_revenue
    , f.actual_cost
    , f.actual_margin
    , f.forecasted_revenue
    , f.forecasted_cost
    , f.forecasted_margin
    , f.confidence_score
    , f.forecast_date
    , f.trend_factor
from orders o
    left join products p on p.product_id = o.product_id
    left join customers c on c.customer_id = o.customer_id
    left join forecasts f on f.year_month = o.year_month
        and f.product_id = p.product_id
where o.order_date >= curdate() - interval 5 year
order by o.order_date desc