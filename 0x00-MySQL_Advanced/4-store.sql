-- using triggers to trigger a procedure

DELIMITER $$
CREATE TRIGGER `new_orders`
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET items.quantity = items.quantity - New.number
    WHERE items.name = New.item_name;
END$$
DELIMITER ;