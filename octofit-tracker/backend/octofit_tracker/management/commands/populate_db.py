
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Ensure unique index on email using pymongo
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db['octofit_tracker_user'].create_index('email', unique=True)

        # Sample users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Sample teams
        teams = [
            Team(name='Marvel', members=['Iron Man', 'Captain America']),
            Team(name='DC', members=['Wonder Woman', 'Batman']),
        ]
        Team.objects.bulk_create(teams)

        # Sample activities
        activities = [
            Activity(user='Iron Man', activity='Running', duration=30),
            Activity(user='Wonder Woman', activity='Cycling', duration=45),
        ]
        Activity.objects.bulk_create(activities)

        # Sample leaderboard
        leaderboard = [
            Leaderboard(team='Marvel', points=100),
            Leaderboard(team='DC', points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Sample workouts
        workouts = [
            Workout(user='Batman', workout='Pushups', reps=50),
            Workout(user='Captain America', workout='Squats', reps=60),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
