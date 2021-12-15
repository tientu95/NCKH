<?php
   if(isset($_FILES['fileUpload'])){
      $errors= array();
      $file_name = $_FILES['fileUpload']['name'];
      $file_size = $_FILES['fileUpload']['size'];
      $file_tmp = $_FILES['fileUpload']['tmp_name'];
    //   $file_type = $_FILES['fileUpload']['type'];
      $file_ext=strtolower(end(explode('.',$_FILES['fileUpload']['name'])));
       
      $expensions= array("pdf","rar","zip");
      $acess_save = "OldPDF/".basename($_FILES["fileUpload"]["name"]);
      
      if ($file_name=="") {
         echo "
        <script type='text/javascript'>
            window.alert('Bạn chưa chọn file');
            window.location.href='check_plagia.php';
        </script>

        ";

      }
      if(in_array($file_ext,$expensions)=== false){
         $errors[]="Chỉ hỗ trợ upload file pdf, rar, zip.";
         echo "
        <script type='text/javascript'>
            window.alert('Chỉ hỗ trợ upload file pdf, rar, zip');
            window.location.href='check_plagia.php';
        </script>

         ";
      }
       
      if($file_size > 2097152) {
         $errors[]='Kích thước file không được lớn hơn 2MB';
      }
       
      if(empty($errors)==true) {
         move_uploaded_file($file_tmp, $acess_save);
        //  echo "Success";
        echo "
        <script type='text/javascript'>
            window.location.href='check_plagia.php';
        </script>

        ";
      }else{
         print_r($errors);
      }
                                                                  }
   
?>