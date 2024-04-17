const {Router}=require("express");
const auth=require("../Middlewares/auth")
const authController = require("../Controllers/Controllers");
const router=Router();

//Route handelling
router.post("/sellersignup",authController.seller_signup_post)
router.post("/sellerlogin",authController.seller_login_post)
router.post("/sellerlogout",authController.seller_logout_post)
router.put("/sellerupdate",auth,authController.updateSeller_put)
router.post("/forgotpassword", authController.forgotPassword)
router.post("/resetpassword", authController.resetPassword)

module.exports=router