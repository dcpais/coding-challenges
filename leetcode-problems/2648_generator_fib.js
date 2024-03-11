/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let xn = 1
    let xn_1 = 1
    let xn_2 = 0

    while (true) {
        yield xn_2;
        xn_2 = xn_1
        xn_1 = xn
        xn = xn_1 + xn_2
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */