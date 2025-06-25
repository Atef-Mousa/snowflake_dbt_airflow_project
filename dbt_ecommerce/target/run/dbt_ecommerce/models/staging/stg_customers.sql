
  create or replace   view ECOMMERCE_DB.ANALYTICS.stg_customers
  
   as (
    SELECT *
FROM raw.customers
  );

