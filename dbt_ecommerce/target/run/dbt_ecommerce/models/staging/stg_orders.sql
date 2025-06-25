
  create or replace   view ECOMMERCE_DB.ANALYTICS.stg_orders
  
   as (
    SELECT *
FROM raw.orders
  );

