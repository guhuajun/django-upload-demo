<style scoped lang="less">
    .index{
        width: 100%;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        h1{
            text-align: center;
            font-size: 24px;
            height: 30px;
        }
        p {
            font-size: 14px;
        }
        img {
            width: 100%;
            height: auto;
        }
        .demo-carousel {
            background-color: lightgray;
            height: 400px;
        }
    }
</style>
<template>
    <div class="index">
        <Row type="flex" justify="center">
            <Col span="24">
                <h1>
                    <p>文件上传示例</p>
                </h1>
            </Col>
        </Row>
        <Row type="flex">
            <Col span="24">
                <p>在单体应用中，很常见的一个业务场景是上传文件。单体应用通常会把文件存放在服务器本地文件夹中。</p>
                <p>有状态容器存储（PX）可以较好的缓解单体应用向云原生应用演进过程中存在的这一问题。</p>
                <p>实际上对云原生应用而言，应该利用对象存储来保存用户上传的文件，而非本地文件夹。</p>
            </Col>
        </Row>
        <Row type="flex">
            <Col span="24">
                <Carousel v-model="value1" loop>
                    <CarouselItem v-for="item in items" :key=item.url>
                        <div class="demo-carousel">
                            <img :src="item.url" />
                        </div>
                    </CarouselItem>
                </Carousel>
            </Col>
        </Row>
        <Row type="flex" justify="center" align="middle">
            <Col span="24">
                <h2>
                <Upload multiple type="drag" action="http://localhost:8000/api/photo/"
                        show-upload-list=false name="photo"
                        :on-error="handleError" :before-upload="handleBeforeUpload">
                    <div style="padding: 20px 0">
                    <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                    <p>单击或拖曳到此处上传图片</p>
                    </div>
                </Upload>
                </h2>
            </Col>
        </Row>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                value1: 0,
                items: [
                    {"url": "http://localhost:8000/media/uploads/2019/02/14/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE1.png"},
                    {"url": "http://localhost:8000/media/uploads/2019/02/14/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE5.png"},
                ]
            }
        },
        methods: {
            handleStart () {
                this.$Modal.info({
                    title: 'Bravo',
                    content: 'Now, enjoy the convenience of iView.'
                });
            }
        }
    }
</script>
