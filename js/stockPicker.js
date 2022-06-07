exports.picker = function (prices) {
    let arr = []
    let count = 0
    for (let i = 0; i < prices.length; i++) {
        for (let j = i + 1; j < prices.length; j++) {
            if (prices[i] < prices[j]) {
                if (prices[j] - prices[i] > count) {
                    count = prices[j] - prices[i]
                    arr.pop()
                    arr.push([i, j])
                }
            } else {
                continue
            }
        }
    } return arr.flat()
}

