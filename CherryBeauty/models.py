
from ast import mod
import profile
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Model
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    """
    Một lớp để đại diện cho bài viết.

    ...

    Thuộc tính
    ----------
    
    title: str
        Tên tiêu đề của bài viết
    header_image: str
        lưu địa chỉ hình ảnh đại diện
    slug: str
        địa chỉ bài viết
    intro: str
        giới thiệu bài viết
    body: str
        nội dung bài viết
    date_added: datetime
        thời gian up bài viết
    likes: models.User
        liên kết đến User like bài viết

    Phương pháp
    -------
    total_likes():
        Đếm số người like bài viết
    headerimageURL():
        địa chỉ hình ảnh đại diện 
    """
    
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True, upload_to="images/blog/")
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextUploadingField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    @property
    def total_likes(self):

        """
        Đếm số người like bài viết.

        Returns
        -------
        likes.count (int): số lượng người like bài viết.
        """

        return self.likes.count()

    class Meta:
        ordering = ['-date_added']
    @property
    def headerimageURL(self):

        """
        Địa chỉ hình ảnh đại diện.

        Returns
        -------
        url(str): địa chỉ hình ảnh bài viết.
        """ 

        try:
            url = self.header_image.url
        except:
            url = ''
        return url

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)

class Like(models.Model):

    """
    Like bài viết.

    ...

    Thuộc tính
    ----------
    
    user: model
        tài khoản người dùng
    post: model
        bài viết
    value: boolean
        trạng thái like hoặc unlike bài viết

    Phương pháp
    -------
    __str__():
        tên
    """

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):

        """
        Tên.

        Returns
        -------
        str(str): Tên bài viết.
        """ 

        return str(self.post)




class Collection(models.Model):

    """
    Lớp đại diện cho bộ sưu tập.

    ...

    Thuộc tính
    ----------
    
    title: str
        Tên bộ sưu tập

    Phương pháp
    -------
    __str__():
        trả về tên bộ sưu tâp
    """

    title = models.CharField(max_length=255)

    def __str__(self):
        """
        Tên.

        Returns
        -------
        str(str): Tên bộ sưu tập.
        """ 
        return self.title

class Brand(models.Model):

    """
    Lớp đại diện cho thương hiệu.

    ...

    Thuộc tính
    ----------
    
    title: str
        Tên bộ nhãn hiệu.

    Phương pháp
    -------
    __str__():
        trả về tên nhãn hiệu
    """

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "brand_img/")

    def __str__(self):
        """
        Tên.

        Returns
        -------
        str(str): Tên nhãn hiệu.
        """ 
        return self.title

class Nation(models.Model):

    """
    Lớp đại diện cho quốc gia.

    ...

    Thuộc tính
    ----------
    
    title: str
        Tên bộ quốc gia.

    Phương pháp
    -------
    __str__():
        trả về tên quốc gia
    """

    title = models.CharField(max_length=255)

    def __str__(self):
        """
        Tên.

        Returns
        -------
        str(str): Tên quốc gia.
        """ 
        return self.title

class Tag(models.Model):

    """
    Lớp đại diện cho loại sản phẩm.

    ...

    Thuộc tính
    ----------
    
    title: str
        Tên loại sản phẩm

    Phương pháp
    -------
    __str__():
        trả về tên loại sản phẩm
    """

    title = models.CharField(max_length=255) 
    def __str__(self):
        """
        Tên.

        Returns
        -------
        str(str): Tên loại sản phẩm.
        """ 
        return self.title 

class Product(models.Model):

    """
    Lớp đại diện cho sản phẩm.

    ...

    Thuộc tính
    ----------
    
    title: str
        tên sản phẩm 
    product_img: image
        hình sản phẩm
    slug: str
        địa chỉ sản phẩm
    collection: model
        bộ sưu tập
    tag: model
        loại sản phẩm
    info: str
        giới thiệu sản phẩm
    body:str
        thông tin sản phẩm
    price: decimal
        giá sản phẩm
    brand: model
        thương hiệu
    nation: model
        quốc gia sản phẩm
    date_added: datetime
        thời gian thêm sản phẩm
    is_sell: boolean
        trạng thái còn hàng

    Phương pháp
    -------
    __str__():
        trả về tên sản phẩm
    """    

    title = models.CharField(max_length=255)
    product_img = models.ImageField(null=True,blank=True, upload_to="product_img/") 
    slug = models.SlugField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE,blank=True,null=True)
    info = models.TextField(blank=True,null=True)
    body = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=3, max_digits=15)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True) 
    is_sell = models.BooleanField(default=True)

    def __str__(self):
        """
        Tên.

        Returns
        -------
        str(str): Tên sản phẩm.
        """ 
        return self.title


class Customer(models.Model):

    """
    Lớp đại diện cho khách hàng.

    ...

    Thuộc tính
    ----------
    
    user: model
        tài khoản khách hàng
    bio: str
        giới thiệu
    profile_pic: image
        hình đại diện khách hàng
    name: str
        họ và tên khách hàng
    email: str
        email khách hàng
    address: str
        địa chỉ khách hàng
    phone_number: str
        số điện thoại khách hàng

    Phương pháp
    -------
    __str__():
        trả về tên khách hàng
    """    


    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/customer/profile_pic")
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=255,null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True, null=True) # validators should be a list

    def __str__(self):
        """
        Tên.

        Returns
        -------
        str(str): Tên khách hàng.
        """ 
        return self.name

class Order(models.Model):
    """
    Lớp đại diện cho đơn hàng.

    ...

    Thuộc tính
    ----------
    
    customer: model
        khách hàng
    date_ordered: datetime
        ngày đặt hàng
    complete: boolean
        trạng thái đơn hàng
    transaction_id: str

    Phương pháp
    -------
    __str__():
        trả về tên khách hàng
    shipping():
        trả về tình trang giao hàng
    get_cart_total():
        trả về tổng số lượng sản phẩm trong giỏ hàng
    get_cart_items():
        trả về tổng giá tiền của giỏ hàng
    """    
    
    customer = models.OneToOneField(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        """
        Tên.

        Returns
        -------
        str(int): id đơn hàng.
        """ 
        return str(self.id)

    @property
    def shipping(self):
        """
        Tình trạng giao hàng.

        Returns
        -------
        shipping(int): Tình trang giao hàng .
        """ 

        shipping = False
        orderitems = self.orderitem_set.all()
        
        return shipping

    @property
    def get_cart_total(self):
        """
        Tính tổng số lượng sản phẩm trong giỏ hàng

        Returns
        -------
        total (int): Tổng số lượng sản phẩm trong giỏ hàng.
        """ 
        orderitems = self.oderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        """
        Tính tổng giá tiền của giỏ hàng

        Returns
        -------
        total (int): Tổng giá tiền của giỏ hàng
        """ 
        orderitems = self.oderitem_set.all()
        total = sum([item.quantily for item in orderitems])
        return total 

class OderItem(models.Model):
    """
    Lớp đại diện cho item trong đơn hàng.

    ...

    Thuộc tính
    ----------
    
    product: model
        sản phẩm
    order: model
        đơn hàng
    quantily: int
        số lượng sản phẩm
    date_added: datetime
        ngày thêm vào giỏ hàng

    Phương pháp
    -------
    get_total():
        trả về tổng giá tiền của một loại sản phẩm
    """
    
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantily = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        """
        Tính tổng giá tiền của một loại sản phẩm

        Returns
        -------
        total (int): Tổng giá tiền của một loại sản phẩm
        """ 
        total = self.product.price * self.quantily
        return total

class City(models.Model):
    """
    Lớp đại diện cho thành phố.

    ...

    Thuộc tính
    ----------
    
    title: str
        Tên thành phố.

    Phương pháp
    -------
    __str__():
        trả về tên thành phố.
    """

    title = models.CharField(max_length=255)

    def __str__(self):
        """
        Tên.

        Returns
        -------
        title(str): Tên thành phố.
        """ 
        return self.title

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True)
    state = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """
        Tên.

        Returns
        -------
        str(str): địa chỉ giao hàng.
        """ 

        return self.address 

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """
        Tên.

        Returns
        -------
        str(str): tên user.
        """ 

        return self.user.username
    