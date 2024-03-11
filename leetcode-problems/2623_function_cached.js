/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = {}
    
    return function(...args) {
        let cacheKey = JSON.stringify(args);
        if (cacheKey in cache) {
            return cache[cacheKey];
        }

        let result = fn(...args)
        cache[cacheKey] = result
        return result
    }

}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */