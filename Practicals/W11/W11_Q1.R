# x and y = Shape coordinates
x <- rep(1:5, times = 6) # Times repeats the sequence
y <- rep(6:1, each = 5) # Each repeats the number

plot(x, y, pch = 0:30, cex = 2.5,
     yaxt = "n", xaxt = "n",
     ann = FALSE, xlim = c(0.5, 5.25),
     ylim = c(0.5, 6.5))

# Positions text to the left of the points (0.6 is closer to the left than 1, for instance)
x2 <- rep(seq(0.6, 4.6, 1), times = 6)
y2 <- rep(6:1, each = 5)

# Labels the 26 coordinates 0 through 25
text(x2[1:26], y2[1:26], 0:25)
