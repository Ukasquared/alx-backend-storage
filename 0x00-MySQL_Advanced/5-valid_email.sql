-- validate email
DELIMITER $$
CREATE TRIGGER validate
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN 
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 1 - OLD.valid_email;
    END IF;
END$$
DELIMITER ;