-- If Then — CC:Tweaked
-- Only dig if there is a block in front.

if turtle.detect() then
    turtle.dig()
    turtle.forward()
    print("Dug and moved.")
end
