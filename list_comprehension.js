const num = "1234-5";
const forbidden = "-";

const result = num.split("").filter((e, i) => e !== forbidden);
console.log(result);
