# from accounts.models import Account
# from subscribers.models import InternalSubscriber
# def create_internal_subscriber(acc_id,email_inetrnal_subscriber,inetrnal_subscriber_name):
#     try:
#         account = Account.objects.get(id=acc_id)
#         internal_subscriber = InternalSubscriber(account_id=account.id, email=email_inetrnal_subscriber, name=inetrnal_subscriber_name, notification_options=None)
#         internal_subscriber.save()
#     except Account.DoesNotExist:
#         return "Account not found!"
#     print("InternalSubscriber created!!")
# create_internal_subscriber('32594','nora@clearmedia.be','nora');
# create_internal_subscriber('32594','paul@clearmedia.be','paul');





from accounts.models import Account
from subscribers.models import InternalSubscriber
def create_internal_subscriber(acc_id,email_internal_subscriber,internal_subscriber_name):
    try:
        account = Account.objects.get(id=acc_id)
        internal_subscriber = InternalSubscriber(account_id=account.id, email=email_internal_subscriber, name=internal_subscriber_name)
        internal_subscriber.save()
        print("InternalSubscriber created!!")
    except Exception as e:
        print (e)
create_internal_subscriber('1','nora@clearmedia.be','Nora');



# >>> create_internal_subscriber('1','nora@gmail.com','nodnkjndjknra');
# InternalSubscriber created!!
# >>> create_internal_subscriber('1','nora@gmail.com','Nora');
# Account matching query does not exist.