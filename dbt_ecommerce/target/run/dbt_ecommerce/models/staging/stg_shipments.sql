
  create or replace   view ECOMMERCE_DB.ANALYTICS.stg_shipments
  
   as (
    SELECT *
FROM raw.shipments
  );

