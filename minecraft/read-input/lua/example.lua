-- Read Input — CC:Tweaked
-- Ask the player how many blocks to dig, then do it.

print("How many blocks shall I dig?")
local n = tonumber(read())

for i = 1, n do
    turtle.dig()
    turtle.forward()
end

print("Done!")
