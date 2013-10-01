from django.test import TestCase
from django.utils import timezone as tz
from django.core.urlresolvers import reverse
from polls.models import Poll
import datetime as dt

class PollMethodTests(TestCase):
	
	def test_was_published_recently_with_future_poll(self):
		"""
		should return false if published in future
		"""
		future_poll = Poll(pub_date=tz.now() + dt.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(), False)

	def test_was_published_recently_with_old_poll(self):
		"""
		false if older than one day
		"""
		old_poll = Poll(pub_date = tz.now() - dt.timedelta(days=30))
		self.assertEqual(old_poll.was_published_recently(), False)
		
	def test_was_published_recently_with_recent_poll(self):
		"""
		true if pub_date was within last day
		"""
		recent_poll = Poll(pub_date = tz.now() - dt.timedelta(hours=1))
		self.assertEqual(recent_poll.was_published_recently(), True)
		
def create_poll(question, days):
	"""
	create poll with given question published the number of 
	days offset to now (negative for polls published in past,
	positive for polls that have yet to be publised)
	"""
	return(Poll.objects.create(question=question,
		pub_date=tz.now() + dt.timedelta(days=days)))
		
class PollViewTests(TestCase):
	def test_index_view_with_no_polls(self):
		"""
		if no polls exist, an appopriate message should be displayed
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_poll_list'], [])
	
	def test_index_view_with_past_poll(self):
		"""
		Polls with a pub_date in the past should be displayed on the 			index page. """
		create_poll(question="Past poll.", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_poll_list'],
			['<Poll: Past poll.>'],
		)
		
	def test_index_view_with_future_poll(self):
		"""
		Polls with a pub_date in the future should not be displayed on 			the index page.
		"""
		create_poll(question="Future poll", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.",
		status_code=200)
		self.assertQuerysetEqual(response.context['latest_poll_list'],
		[])
	
	def test_index_view_with_future_poll_and_post_polls(self):
		"""
		Even if both past and future polls exist, only past polls 			should be displayed.
		"""
		create_poll(question="Past poll.", days=-30)
		create_poll(question="Future poll", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_poll_list'],
			['<Poll: Past poll.>']
		)
	
	def test_index_view_with_two_past_polls(self):
		"""
		The polls index page may display multiple polls. """
		create_poll(question="Past poll 1.", days=-30)
		create_poll(question="Past poll 2.", days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_poll_list'],
			['<Poll: Past poll 1.>', '<Poll: Past poll 2.>']
		)
		
class PollIndexDetailTest(TestCase):
	
	def test_detail_view_with_a_future_poll(self):
		""" Detail view of poll with future pub_date
		should be 404 """
		future_poll = create_poll(question='Future poll.', days=5)
		response = self.client.get(reverse('polls:detail', args=(future_poll.id,)))
		self.assertEqual(response.status_code, 404)
		
	def test_detail_view_with_a_past_poll(self):
		#past poll displays questions
		past_poll = create_poll(question='Past Poll',
		days=-5)
		response.self.client.get(reverse('polls:detail', args=(past_poll.id,)))
		self.assertContains(response, past_poll.question, status_code=200)
		
		
		
		
		
		
		
