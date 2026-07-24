-- Functions — CC:Tweaked
-- Write a function once, call it as many times as you like.

local function stepForward()
    turtle.dig()
    turtle.forward()
end

for i = 1, 5 do
    stepForward()
end
