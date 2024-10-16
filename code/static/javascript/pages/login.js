<script src="../plug-ins/layerUi/layer.js"></script>
$(function(){
    $('#entry').click(function(){
        var adminName = $('#adminName').val();
        var adminPwd = $('#adminPwd').val();
        if(adminName == ''){
            //$('.mask,.dialog').show();
            //$('.dialog .dialog-bd p').html('请输入管理员账号');
            layer.msg('玩命提示中', {time: 800});
        }else if(adminPwd == ''){
            // $('.mask,.dialog').show();
            // $('.dialog .dialog-bd p').html('请输入管理员密码');
            layer.msg('玩命提示中', {time: 800});
        }else{
            // 使用 AJAX 发送 POST 请求
            $.ajax({
                url: '/login',  // Flask 路由
                type: 'POST',
                data: {
                    adminName: adminName,
                    adminPwd: adminPwd
                },
                success: function(response) {
					if(response.status == 'success') {
                        window.location.href = response.redirect_url; // 登录成功，跳转到主页
                    } else {
                        // $('.mask,.dialog').show();
                        // $('.dialog .dialog-bd p').html('用户名或密码错误');
                        layer.msg('玩命提示中', {time: 800});
                    }
                }
            });
        }
    });
});