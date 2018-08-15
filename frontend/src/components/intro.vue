<template>
  <div id="body">
    <div class="toolbar">
      <table align="right">
        <tr>
          <td>
            <el-button class="user-ope" type="text" v-if="login" @click="loginFormVisible = true" style="color:#085078;font-size:18px">登录&nbsp;&nbsp;&nbsp;</el-button>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="login" @click="registerFormVisible = true" style="color:#085078;font-size:18px">注册</el-button>
          </td>
          <td>
            <el-button class="user-ope" type="text" v-if="not_login" @click="logout" style="color:white">登出</el-button>
          </td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
      </table>
    </div>

    <div class="logindialog">
      <el-dialog title="登录" :visible.sync="loginFormVisible" width="400px" height="700px">
        <el-form :model="loform" :rules="rules">
          <el-form-item label="手机号" :label-width="loginLabelWidth" prop="lophone">
            <el-col :span="18">
              <el-input v-model="loform.phonenumber" auto-complete="true" clearable required="required" pattern="/^1[3|4|5|7|8][0-9]\d{8}$/" oninvalid="this.setCustomValidity('warning')"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="验证码" :label-width="loginLabelWidth">
            <el-col :span="18">
              <el-input v-model="loform.password" auto-complete="off" clearable></el-input>
            </el-col>
          </el-form-item>
        </el-form>
        <div slot="footer" class="login-footer">
          <el-button type="primary" @click="loginFormVisible = false">获取验证码</el-button>
          <el-button @click="loginFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="loginFormVisible = false">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div class="registerdialog">
      <el-dialog title="注册" :visible.sync="registerFormVisible" width="400px" height="700px">
        <el-form :model="reform" :rules="rules">
          <el-form-item label="手机号" :label-width="registerLabelWidth" prop="rephone">
            <el-col :span="18">
              <el-input v-model="reform.phonenumber" auto-complete="off" clearable required="required" pattern="/^1[3|4|5|7|8][0-9]\d{8}$/"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="验证码" :label-width="registerLabelWidth">
            <el-col :span="18">
              <el-input v-model="reform.password" auto-complete="off" clearable></el-input>
            </el-col>
          </el-form-item>
        </el-form>
        <div slot="footer" class="register-footer">
          <el-button type="primary" @click="loginFormVisible = false">获取验证码</el-button>
          <el-button @click="registerFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="registerFormVisible = false">确 定</el-button>
        </div>
      </el-dialog>
    </div>

    <div style="text-align: center; margin:0px; ">
      <img alt="" :src="picture" width="700" height="400"/>
    </div>
    <div id="page">
      <div id="class">课程 {{ title }}</div>
      <div class= "money" v-if = "moneyFlag">￥{{ money }}</div>
      <div class= "money" v-else>免费课程</div>
      <p class="classContent">{{ classIntro }}</p>
      <div class="operate">
          <el-button type="danger" plain v-if = "burnedFlag">已焚毁</el-button>
          <el-button type="success" v-else-if = "moneyFlag==0">立即观看</el-button>
          <el-button type="success" v-else-if = "paidFlag">立即观看</el-button>
          <el-button type="primary" v-else-if = "paidFlag==0" @click="payDialogVisible = true">去支付</el-button>
          <el-button type="primary" icon="el-icon-share" @click.native="shareDialogVisible = true"></el-button>
      </div>
    </div>

    <div class = "payDialog">
      <el-dialog title="支付" :visible.sync="payDialogVisible" width="500px" height="400px">
        <div id="paymoney">课程金额：￥{{ money }}</div>
        <el-button  class="pay" type="primary" round>支付宝支付</el-button><br />
        <el-button  class="pay" type="primary" round v-if ="bountyFlag">赏金支付</el-button>
        <el-button  class="pay" type="primary" round v-else disabled>赏金不足</el-button>
        <span id="account">当前赏金： {{ bounty }}</span>
      </el-dialog>
    </div>

     <div class = "shareDialog">
      <el-dialog title="分享" :visible.sync="shareDialogVisible" width="400px" height="400px">
        <div style="text-align: center;">
          <div id="shareText">分享途径</div>
          <el-button class="share" type="primary" round>微信分享</el-button><br />
          <el-button class="share" type="primary" round>QQ分享</el-button><br />
        </div>
      </el-dialog>
    </div>

    <div>
      <router-link to="/coursepage">
        <button>进入课程</button>
      </router-link>
    </div>
    <br />
    <el-footer height="50px">2100实验室 联系电话：010-86398756 关注我们：微信服务号：科学队长</el-footer>

  </div>
</template>

<script>
export default {
  data() {
    var phoneReg = /^1[3|4|5|7|8][0-9]\d{8}$/
    var validateloPhone = (rule, value, callback) => {
      if (!this.loform.phonenumber) {
        return callback(new Error('号码不能为空'))
      }
      setTimeout(() => {
        if (!phoneReg.test(this.loform.phonenumber)) {
          callback(new Error('格式有误'))
        } else {
          callback()
        }
      }, 100)
    }
    var validaterePhone = (rule, value, callback) => {
      if (!this.reform.phonenumber) {
        return callback(new Error('号码不能为空'))
      }
      setTimeout(() => {
        if (!phoneReg.test(this.reform.phonenumber)) {
          callback(new Error('格式有误'))
        } else {
          callback()
        }
      }, 100)
    }
    return {
      buttonShow: '观看',
      title: '我们爱科学',
      // burnedFlag表示当前是否焚毁（true为已焚毁）
      burnedFlag: false,
      // money表示当前课程的价钱，moneyFlag表示该课是否免费（true为付费 false为免费）
      moneyFlag: true,
      money: '25',
      // paidFlag表示当前用户是否已支付该课程(true 表示已支付)
      paidFlag: false,

      classIntro: '在十九课里，我们学到了赵州桥是多么的雄伟、壮观。想一想，以前的桥就让我们赞不绝口，未来的桥会是怎样的呢？开动你的小脑筋，仔细想一想吧在未来的世界里，桥是透明的，看不见，摸得着。一辆辆车以最快的速度冲向桥，都想争夺第一个飞马王子。原来啊，由于桥是透明的，看不见桥，只能看见一辆辆在桥上飞奔的汽车，所以就像车在天上飞一样。在桥上的人和汽车，既能看见远处的风景，让自己欣赏，又能让别人看了以为是在天上飞的汽车，让他们赞叹不已。这就是未来的桥，一个桥上的创举。在十九课里，我们学到了赵州桥是多么的雄伟、壮观。想一想，以前的桥就让我们赞不绝口，未来的桥会是怎样的呢？开动你的小脑筋，仔细想一想吧在未来的世界里，桥是透明的，看不见，摸得着。一辆辆车以最快的速度冲向桥，都想争夺第一个飞马王子。原来啊，由于桥是透明的，看不见桥，只能看见一辆辆在桥上飞奔的汽车，所以就像车在天上飞一样。在桥上的人和汽车，既能看见远处的风景，让自己欣赏，又能让别人看了以为是在天上飞的汽车，让他们赞叹不已。这就是未来的桥，一个桥上的创举。',
      picture: require('../assets/class2.jpg'),

      // 支付框是否显示
      payDialogVisible: false,
      // 当前用户赏金
      bounty: 15,
      // 当前赏金是否可以购买课程（true为可购买）
      bountyFlag: false,

      // 分享框是否显示
      shareDialogVisible: false,

      login: true,
      not_login: false,
      loginFormVisible: false,
      loginLabelWidth: '100px',
      loform: {
        phonenumber: '',
        password: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      registerFormVisible: false,
      registerLabelWidth: '100px',
      reform: {
        phonenumber: '',
        password: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      rules: {
        lophone: [{ required: true, validator: validateloPhone, trigger: 'blur' }],
        rephone: [{ required: true, validator: validaterePhone, trigger: 'blur' }]
      }
    }
  },
  methods: {
    handleChange(value) {
      console.log(value)
    }
  }
}
</script>
<style>
  .toolbar {
    width: 100%;
    height: 55px;
    margin: 0;
    padding: 0;
    text-align: right;
    background-color:lightskyblue;
    background: linear-gradient(lightskyblue, white);
    opacity: 0.7;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }
  #class {
    font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;
    font-size: 30px;
    font-weight: bold;
    padding-bottom: 30px;
  }
  .money {
    color: red ;
    font-size: 25px;
    font-weight: bold;
    letter-spacing: 0;
    padding-bottom: 20px;
  }
  #page {
    width: 600px;
    margin:0px auto 0px auto;
    padding:40px;
    border-left-style: solid;
    border-left-width: 1px;
    border-right-style: solid;
    border-right-width: 1px;
    border-bottom-style: solid;
    border-bottom-width: 1px;
  }
  .classContent {
    text-indent: 2em;
    margin-bottom: 40px;
    letter-spacing: 0.2em;
    font-size: 16px;
  }
  .el-button {
    margin-right: 40px;
    width: 100px;
    height:  40px;
  }
  .el-icon-share {
    width: 20px;
    height:30px;
  }
  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 55px;
    background-color:lightskyblue;
    background: linear-gradient(white, lightskyblue);
    opacity: 0.7;
  }
  .pay {
    margin:20px;
    margin-left: 40px;
    width:150px;
    height: 45px;
  }
  .el-dialog__body {
    padding-top: 20px;
  }
  #paymoney {
    font-size: 24px;
    margin-bottom: 40px;
    margin-left: 50px;
    margin-top: 0px;
    font-weight: bold;
  }
  #account {
    margin-left: 15px;
    font-size: 15px;
  }
  #shareText {
    font-size: 24px;
    font-weight: bold;
    margin: 20px;
  }
  .share {
    margin:20px;
    width:150px;
    height: 45px;
  }

</style>
