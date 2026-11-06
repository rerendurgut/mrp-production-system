DELIMITER $$

CREATE PROCEDURE GetRequiredItemsCount(
    IN item VARCHAR(16),
    IN parent_item_count INT,
    IN parent_item_due INT
)
BEGIN
    -- CLEAR THE REQUIRED ITEMS TABLE
    DELETE FROM required_items;
    
    INSERT INTO required_items (required_item, required_amount, due_period)
    
        WITH RECURSIVE cte (it, ad, due) AS (
            SELECT DISTINCT bom.item_id, parent_item_count, parent_item_due
            FROM bom 
            WHERE bom.item_id = item
            UNION ALL
            SELECT bom.component_id, cte.ad * bom.bom_multiplier, cte.due - GetLeadTime(cte.it)
            FROM cte
            JOIN bom ON cte.it = bom.item_id
        )
        SELECT it AS required_item, ad AS required_amount, due AS due_period
        FROM cte
        ORDER BY it;

END $$

DELIMITER;
