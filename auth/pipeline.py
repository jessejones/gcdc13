from django.shortcuts import redirect

from social.pipeline.partial import partial


@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
  if user and user.email:
      return
  elif is_new and not details.get('email'):
      if strategy.session_get('saved_email'):
          details['email'] = strategy.session_pop('saved_email')
      else:
          return redirect('require_email')

@partial
def verify_password(strategy, user, is_new=False, *args, **kwargs):
	if user.has_usable_password():
		return
	else:
	  return redirect('signup_username')

def user_password(strategy, user, is_new=False, *args, **kwargs):
	if strategy.backend.name != 'username':
		return

	password = strategy.request_data()['password']
	if not user.has_usable_password():
		user.set_password(password)
		user.save()
	elif not user.check_password(password):
		raise AuthException(strategy.backend)