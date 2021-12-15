<meta charset="UTF-8" />
<?php
    include('config.php');
    $to      = (string)$_POST['txtEmail'];
    $subject = 'Chào mừng đến với ....';
    $message = 'Bạn đã đăng ký thành công '."\n"
                ."\n".'     Mọi thông tin chi tiết vui lòng liên hệ:'
                ."\n".'     Hotline: 024 3825 5599'
                ."\n".'     Email: Check@gmail.com'
                ."\n".'     Đ/c: Ngõ 12, Chùa Bộc, Đống Đa, Hà Nội';        
    






    mail($to,$subject,$message);
    echo "
            <script type='text/javascript'>
                window.alert('Bạn đã đăng ký thành công');
                window.location.href='index.php'
            </script>
        ";
    
?>
