-- Detect Blocks — CC:Tweaked
-- Check if there is a block in front before trying to dig.

if turtle.detect() then
    turtle.dig()
    turtle.forward()
else
    print("Nothing to dig here.")
end
