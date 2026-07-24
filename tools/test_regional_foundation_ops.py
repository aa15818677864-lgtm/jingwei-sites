import copy
import unittest

from regional_foundation_ops import TOPICS, audit, build_plan, review_errors


class RegionalFoundationOpsTests(unittest.TestCase):
    def test_topic_matrix_has_fifty_per_region(self):
        self.assertEqual({region: 50 for region in TOPICS}, {region: len(items) for region, items in TOPICS.items()})

    def test_replaced_cross_region_duplicate_does_not_return(self):
        co_owned_regions = [
            region
            for region, topics in TOPICS.items()
            if any(item["slug"] == "co-owned-mainland-property" for item in topics)
        ]
        self.assertEqual(["SG"], co_owned_regions)
        self.assertIn(
            "omitted-heir-after-macau-qualification-deed",
            {item["slug"] for item in TOPICS["MO"]},
        )
        self.assertIn(
            "california-inventory-mainland-property-value",
            {item["slug"] for item in TOPICS["US"]},
        )

    def test_seed_plan_passes_audit(self):
        self.assertEqual([], audit(build_plan()))

    def test_ready_story_requires_three_real_reviews(self):
        story = build_plan()["stories"][0]
        broken = copy.deepcopy(story)
        broken["reviews"][1]["problemsFound"] = []
        self.assertTrue(any("problemsFound" in error for error in review_errors(broken)))

    def test_planned_story_does_not_fake_reviews(self):
        story = build_plan()["stories"][2]
        self.assertEqual("planned", story["status"])
        self.assertEqual([], story["reviews"])
        self.assertEqual([], review_errors(story))

    def test_existing_progress_is_preserved(self):
        original = build_plan()
        original["stories"][2]["status"] = "researching"
        original["stories"][2]["research"] = [{"type": "regional-official", "status": "verified"}]
        rebuilt = build_plan(original)
        self.assertEqual("researching", rebuilt["stories"][2]["status"])
        self.assertEqual(original["stories"][2]["research"], rebuilt["stories"][2]["research"])


if __name__ == "__main__":
    unittest.main()
