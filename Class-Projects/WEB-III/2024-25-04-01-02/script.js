function Input() {
    const nums =  [];

    for (let i = 1; i <= 100; i++) {
        nums.push(i);
    }

    return nums;
}





function Sum(input) {
    let sum = 0;

    input.forEach((num) => {
        sum += num;
    });

    return sum;
}






console.log(Sum(Input()));