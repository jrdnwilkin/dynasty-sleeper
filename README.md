
# Limitations
(B) Manually overridden scores are not handled.

1. Copy .env.sample into .env
2. Set API key for sendgrid
3. Install relevant python libraries
4. Set up google cloud authentication (install google cloud cli and set up auth there or add environment variables)

# Player roster calculation

Because weekly matchups don't store taxi squad and ir information, we need to look at rosters once around 2AM tuesday night and save the weekly roster to Google cloud storage. If it exists on cloud storage, we use the existing one instead. If this file gets recreated at a later point, it will likely be wrong. Everything depends on this file. If this is wrong, penalties will need to be determined manually for the week.

# Rule considerations for next year
1. This should look for unique players on the bench to cover. (i.e. if you have 2 zero point WR starters, and 1 eligible WR replacement, you would still get 1 penalty (whereas currently it is 0.)

2. Instead of looking for players with more than zero points on the bench we should look for players with non-zero points (to ensure they played.) 

3. Maybe instead of basing this whole thing on scoring, we base it on snaps played (both for starters and bench considerations). I think this may be able to be determined from sleepers stats api's. Like imagine you play DaVante Adams a week he is starting and he goes 0/6 receptions for 0 yards. You would get a penalty even if was the right play to play him. I don't think that is the intention of this penalties rule. The downside is this information doesn't appear in sleeper ui that I'm aware of, so the only way to confirm this would be by debugging or calling APIs directly (or could use different sources visually, and if it still doesn't match, then debug.)

4. Allow for potential starting roster re-arrangement. For example, say Zeke does not play, but you have him in starting RB spot. Currently you MUST have a valid bench RB or else you are penalized. However, say you had valid bench WRs and another valid RB in a starting flex position. In this case, you could have swapped the starting RB and flex positions and then you would have been fine because your zero scoring roster spot (Zeke) would have been flex, therefore he could have been replaced by the valid bench WR. This would probably be the most involved of all these to implement programatically, but definitely doable.

5. Include taxi squad and IR players as elgiible replacements as the purpose of this rule is to prevent you from tanking max potential points, and those roles already count to max potential points. If we make this change, both limitation (A) and (B) can be removed and (Player roster calculation). If we make this change, base the code off matchups (https://docs.sleeper.app/#getting-matchups-in-a-league) instead of rosters cached weekly.