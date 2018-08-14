<template>
  <div id="body">
    <div style="text-align: center; margin:0px; ">
      <img alt="" :src="picture" width="700" height="400"/>
    </div>
    <div id="page">
      <div id="class">课程 {{ title }}</div>
      <div id= "money"><span id="symbol">￥</span>{{ money }}</div>
      <p class="classContent">{{ classIntro }}</p>
      <div class="operate">
          <el-button type="success">{{ buttonShow }}</el-button>
          <i class="el-icon-share"></i>
      </div>
    </div>
    <div>
      <router-link to="/coursepage">
        <button>进入课程</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      buttonShow: '观看',
      title: '我们爱科学',
      money: '25',
      classIntro: '在十九课里，我们学到了赵州桥是多么的雄伟、壮观。想一想，以前的桥就让我们赞不绝口，未来的桥会是怎样的呢？开动你的小脑筋，仔细想一想吧在未来的世界里，桥是透明的，看不见，摸得着。一辆辆车以最快的速度冲向桥，都想争夺第一个飞马王子。原来啊，由于桥是透明的，看不见桥，只能看见一辆辆在桥上飞奔的汽车，所以就像车在天上飞一样。在桥上的人和汽车，既能看见远处的风景，让自己欣赏，又能让别人看了以为是在天上飞的汽车，让他们赞叹不已。这就是未来的桥，一个桥上的创举。在十九课里，我们学到了赵州桥是多么的雄伟、壮观。想一想，以前的桥就让我们赞不绝口，未来的桥会是怎样的呢？开动你的小脑筋，仔细想一想吧在未来的世界里，桥是透明的，看不见，摸得着。一辆辆车以最快的速度冲向桥，都想争夺第一个飞马王子。原来啊，由于桥是透明的，看不见桥，只能看见一辆辆在桥上飞奔的汽车，所以就像车在天上飞一样。在桥上的人和汽车，既能看见远处的风景，让自己欣赏，又能让别人看了以为是在天上飞的汽车，让他们赞叹不已。这就是未来的桥，一个桥上的创举。',
      picture: require('../assets/class2.jpg')
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
  #class {
    font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;
    font-size: 25px;
    padding-bottom: 10px;
  }
  #money {
    color: red ;
    font-size: 20px;
    font-weight: bold;
    letter-spacing: 0;
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
  }
  .el-icon-share {
    width: 20px;
    height:30px;
  }
</style>
