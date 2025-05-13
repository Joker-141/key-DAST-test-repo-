// eval-based injection
const userCode = "alert('pwned')";
eval(userCode);

// XSS vulnerability
const name = req.query.name;
res.send(`<div>${name}</div>`);
