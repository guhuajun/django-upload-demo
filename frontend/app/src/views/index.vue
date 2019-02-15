<style scoped>
.layout {
  border: 0px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  overflow: hidden;
}
.layout-nav {
  width: 420px;
  margin: 0 auto;
  margin-right: 20px;
}
.layout-logo-text {
  color: white;
  font-size: 24px;
}
.layout-footer-center {
  text-align: center;
}
.demo-carousel {
  max-height: 250px;
}
.demo-carousel-img {
  margin-left: auto;
  margin-right: auto;
  display: block;
}
</style>
<template>
  <div class="layout">
    <Layout>
      <Header>
        <Menu mode="horizontal" theme="dark" active-name="1">
          <div class="layout-logo-text">云原生应用存储演示</div>
        </Menu>
      </Header>
      <Content :style="{padding: '0 50px'}">
        <Breadcrumb :style="{margin: '20px 0'}">
          <BreadcrumbItem>首页</BreadcrumbItem>
          <BreadcrumbItem>照片展示</BreadcrumbItem>
        </Breadcrumb>
        <Card>
          <div>
            <ul>
              <li>在单体应用中，很常见的一个业务场景是上传文件。单体应用通常会把文件存放在服务器本地文件夹中。</li>
              <li>云原生应用存储（PX）可以较好的缓解单体应用向云原生应用演进过程中存在的这一问题。</li>
              <li>实际上对云原生应用而言，应该利用对象存储来保存用户上传的文件，而非本地文件夹。</li>
            </ul>
          </div>
        </Card>
        <Card>
          <div v-if="items.length > 0" style="max-height: 300px;">
            <Carousel v-model="value1" loop>
              <CarouselItem v-for="item in items" :key="item.photo">
                <div class="demo-carousel">
                  <img class="demo-carousel-img" :src="item.photo">
                </div>
              </CarouselItem>
            </Carousel>
          </div>
          <div v-else style="max-height: 300px;">
              <p>还未上传图片，无法进行展示</p>
          </div>
        </Card>
        <Card>
          <div>
            <Upload
              multiple
              type="drag"
              action="api/photo/"
              name="photo"
              :on-success="handleOnSuccess"
            >
              <div style="padding: 20px 0">
                <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                <p>单击或拖曳到此处上传图片</p>
              </div>
            </Upload>
          </div>
        </Card>
      </Content>
      <Footer class="layout-footer-center"></Footer>
    </Layout>
  </div>
</template>
<script>
export default {
  data() {
    return {
      value1: 0,
      items: []
    };
  },
  methods: {
    loadImgs() {
        const _this = this;
        this.$util.ajax.get('api/photo/').then(
            function (response) {
                _this.items = response.data.results;
            }
        )
    },
    handleOnSuccess(response, file, fileList) {
        console.log(file);
        this.loadImgs()
    }
  },
  mounted() {
      this.loadImgs();
  }
};
</script>
