// eval is dangerous
const code = "alert('XSS')";
eval(code);

// hardcoded credentials
const password = "supersecret";

// unescaped user input
const input = req.query.q;
res.send(`<p>${input}</p>`);
