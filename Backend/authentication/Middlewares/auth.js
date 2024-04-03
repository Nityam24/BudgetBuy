const JWT =require("jsonwebtoken");
require("dotenv").config()
const cookieParser = require("cookie-parser")

const JWTverify=async (req,res,next)=>{
    const token=req.cookies.jwt
    if(!token){
        res.status(401).json({message:"no token found"});
    }
    else{
        const decode=JWT.verify(token, process.env.SECRET_KEY)
        req.authdata=decode;
        next();
    }
}
module.exports=JWTverify;