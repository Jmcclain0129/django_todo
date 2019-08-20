{"filter":false,"title":"test_views.py","tooltip":"/todo/test_views.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":31,"column":42},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":210},{"start":{"row":32,"column":0},"end":{"row":32,"column":8},"action":"insert","lines":["        "]},{"start":{"row":32,"column":8},"end":{"row":33,"column":0},"action":"insert","lines":["",""]},{"start":{"row":33,"column":0},"end":{"row":33,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":8},"action":"remove","lines":["    "],"id":211},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":33,"column":0},"end":{"row":36,"column":42},"action":"insert","lines":["    def test_post_create_an_item(self):","        response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})","        item = get_object_or_404(Item, pk=1)","        self.assertEqual(item.done, False)"],"id":212}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":24},"action":"remove","lines":["e"],"id":213},{"start":{"row":33,"column":22},"end":{"row":33,"column":23},"action":"remove","lines":["t"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["a"]},{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"remove","lines":["e"]},{"start":{"row":33,"column":19},"end":{"row":33,"column":20},"action":"remove","lines":["r"]},{"start":{"row":33,"column":18},"end":{"row":33,"column":19},"action":"remove","lines":["c"]}],[{"start":{"row":33,"column":18},"end":{"row":33,"column":19},"action":"insert","lines":["e"],"id":214},{"start":{"row":33,"column":19},"end":{"row":33,"column":20},"action":"insert","lines":["d"]},{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"insert","lines":["i"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":34,"column":8},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":215},{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"insert","lines":["        "]},{"start":{"row":35,"column":8},"end":{"row":36,"column":0},"action":"insert","lines":["",""]},{"start":{"row":36,"column":0},"end":{"row":36,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["i"],"id":216},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["t"]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["e"]},{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["m"]}],[{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":[" "],"id":217},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":[" "],"id":218},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["I"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["t"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["e"]},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["m"]}],[{"start":{"row":34,"column":19},"end":{"row":34,"column":21},"action":"insert","lines":["()"],"id":219}],[{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["n"],"id":220},{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":["a"]},{"start":{"row":34,"column":22},"end":{"row":34,"column":23},"action":"insert","lines":["m"]},{"start":{"row":34,"column":23},"end":{"row":34,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["="],"id":221}],[{"start":{"row":33,"column":0},"end":{"row":38,"column":42},"action":"remove","lines":["    def test_post_edit_an_item(self):","        item = Item(name=)","        ","        response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})","        item = get_object_or_404(Item, pk=1)","        self.assertEqual(item.done, False)"],"id":222},{"start":{"row":33,"column":0},"end":{"row":40,"column":55},"action":"insert","lines":["    def test_get_edit_item_page(self):","        item = Item(name='Create a Test')","        item.save()","        ","        ","        page = self.client.get(\"/edit/{0}\".format(item.id))","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")"]}],[{"start":{"row":33,"column":15},"end":{"row":33,"column":16},"action":"remove","lines":["t"],"id":223},{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"remove","lines":["e"]},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"remove","lines":["g"]}],[{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["p"],"id":224},{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"insert","lines":["o"]},{"start":{"row":33,"column":15},"end":{"row":33,"column":16},"action":"insert","lines":["s"]},{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":24},"action":"insert","lines":["a"],"id":225},{"start":{"row":33,"column":24},"end":{"row":33,"column":25},"action":"insert","lines":["n"]},{"start":{"row":33,"column":25},"end":{"row":33,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":33,"column":34},"end":{"row":33,"column":35},"action":"remove","lines":["e"],"id":226},{"start":{"row":33,"column":33},"end":{"row":33,"column":34},"action":"remove","lines":["g"]},{"start":{"row":33,"column":32},"end":{"row":33,"column":33},"action":"remove","lines":["a"]},{"start":{"row":33,"column":31},"end":{"row":33,"column":32},"action":"remove","lines":["p"]},{"start":{"row":33,"column":30},"end":{"row":33,"column":31},"action":"remove","lines":["_"]}],[{"start":{"row":35,"column":19},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":227},{"start":{"row":36,"column":0},"end":{"row":36,"column":8},"action":"insert","lines":["        "]},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["i"]},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["d"]}],[{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":[" "],"id":228},{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":[" "],"id":229},{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":["i"]},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["t"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["e"]},{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"insert","lines":["m"]}],[{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["."],"id":230},{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"insert","lines":["i"]},{"start":{"row":36,"column":19},"end":{"row":36,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":36,"column":20},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":231},{"start":{"row":37,"column":0},"end":{"row":37,"column":8},"action":"insert","lines":["        "]},{"start":{"row":37,"column":8},"end":{"row":38,"column":0},"action":"insert","lines":["",""]},{"start":{"row":38,"column":0},"end":{"row":38,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":70},"action":"insert","lines":["response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})"],"id":232}],[{"start":{"row":38,"column":70},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":233},{"start":{"row":39,"column":0},"end":{"row":39,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":39,"column":8},"end":{"row":40,"column":42},"action":"insert","lines":["        item = get_object_or_404(Item, pk=1)","        self.assertEqual(item.done, False)"],"id":234}],[{"start":{"row":39,"column":12},"end":{"row":39,"column":16},"action":"remove","lines":["    "],"id":235},{"start":{"row":39,"column":8},"end":{"row":39,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":41,"column":0},"end":{"row":45,"column":55},"action":"remove","lines":["        ","        ","        page = self.client.get(\"/edit/{0}\".format(item.id))","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")"],"id":236},{"start":{"row":40,"column":42},"end":{"row":41,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":[" "],"id":237}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"remove","lines":[" "],"id":238}],[{"start":{"row":40,"column":8},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":239},{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":41,"column":25},"end":{"row":41,"column":34},"action":"remove","lines":["item.done"],"id":240},{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"insert","lines":["\""]},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["A"]}],[{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"insert","lines":[" "],"id":241},{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["d"]},{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"insert","lines":["i"]},{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"insert","lines":["f"]},{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"insert","lines":["f"]},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["e"]},{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["r"]},{"start":{"row":41,"column":34},"end":{"row":41,"column":35},"action":"insert","lines":["e"]},{"start":{"row":41,"column":35},"end":{"row":41,"column":36},"action":"insert","lines":["n"]},{"start":{"row":41,"column":36},"end":{"row":41,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"insert","lines":[" "],"id":242},{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"insert","lines":["n"]},{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":["a"]},{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"insert","lines":["m"]},{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":48},"end":{"row":41,"column":49},"action":"remove","lines":["e"],"id":243},{"start":{"row":41,"column":47},"end":{"row":41,"column":48},"action":"remove","lines":["s"]},{"start":{"row":41,"column":46},"end":{"row":41,"column":47},"action":"remove","lines":["l"]},{"start":{"row":41,"column":45},"end":{"row":41,"column":46},"action":"remove","lines":["a"]},{"start":{"row":41,"column":44},"end":{"row":41,"column":45},"action":"remove","lines":["F"]}],[{"start":{"row":41,"column":44},"end":{"row":41,"column":45},"action":"insert","lines":["i"],"id":244},{"start":{"row":41,"column":45},"end":{"row":41,"column":46},"action":"insert","lines":["t"]},{"start":{"row":41,"column":46},"end":{"row":41,"column":47},"action":"insert","lines":["e"]},{"start":{"row":41,"column":47},"end":{"row":41,"column":48},"action":"insert","lines":["m"]},{"start":{"row":41,"column":48},"end":{"row":41,"column":49},"action":"insert","lines":["."]}],[{"start":{"row":41,"column":49},"end":{"row":41,"column":50},"action":"insert","lines":["n"],"id":245},{"start":{"row":41,"column":50},"end":{"row":41,"column":51},"action":"insert","lines":["a"]},{"start":{"row":41,"column":51},"end":{"row":41,"column":52},"action":"insert","lines":["m"]},{"start":{"row":41,"column":52},"end":{"row":41,"column":53},"action":"insert","lines":["e"]}],[{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"remove","lines":["d"],"id":246},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"remove","lines":["d"]},{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"remove","lines":["a"]}],[{"start":{"row":38,"column":38},"end":{"row":38,"column":39},"action":"insert","lines":["e"],"id":247},{"start":{"row":38,"column":39},"end":{"row":38,"column":40},"action":"insert","lines":["d"]},{"start":{"row":38,"column":40},"end":{"row":38,"column":41},"action":"insert","lines":["i"]},{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":42},"end":{"row":38,"column":43},"action":"insert","lines":["/"],"id":248},{"start":{"row":38,"column":43},"end":{"row":38,"column":44},"action":"insert","lines":["{"]}],[{"start":{"row":38,"column":44},"end":{"row":38,"column":45},"action":"insert","lines":["0"],"id":249}],[{"start":{"row":38,"column":45},"end":{"row":38,"column":46},"action":"insert","lines":["}"],"id":250}],[{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"remove","lines":[","],"id":251}],[{"start":{"row":38,"column":47},"end":{"row":38,"column":48},"action":"insert","lines":["."],"id":252}],[{"start":{"row":38,"column":48},"end":{"row":38,"column":49},"action":"insert","lines":["f"],"id":253},{"start":{"row":38,"column":49},"end":{"row":38,"column":50},"action":"insert","lines":["o"]},{"start":{"row":38,"column":50},"end":{"row":38,"column":51},"action":"insert","lines":["r"]},{"start":{"row":38,"column":51},"end":{"row":38,"column":52},"action":"insert","lines":["m"]},{"start":{"row":38,"column":52},"end":{"row":38,"column":53},"action":"insert","lines":["a"]},{"start":{"row":38,"column":53},"end":{"row":38,"column":54},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":54},"end":{"row":38,"column":56},"action":"insert","lines":["()"],"id":254}],[{"start":{"row":38,"column":55},"end":{"row":38,"column":56},"action":"insert","lines":["i"],"id":255},{"start":{"row":38,"column":56},"end":{"row":38,"column":57},"action":"insert","lines":["d"]}],[{"start":{"row":38,"column":58},"end":{"row":38,"column":59},"action":"insert","lines":[","],"id":256}],[{"start":{"row":38,"column":70},"end":{"row":38,"column":83},"action":"remove","lines":["Create a Test"],"id":257},{"start":{"row":38,"column":70},"end":{"row":38,"column":71},"action":"insert","lines":["A"]}],[{"start":{"row":38,"column":71},"end":{"row":38,"column":72},"action":"insert","lines":[" "],"id":258},{"start":{"row":38,"column":72},"end":{"row":38,"column":73},"action":"insert","lines":["d"]},{"start":{"row":38,"column":73},"end":{"row":38,"column":74},"action":"insert","lines":["i"]},{"start":{"row":38,"column":74},"end":{"row":38,"column":75},"action":"insert","lines":["f"]},{"start":{"row":38,"column":75},"end":{"row":38,"column":76},"action":"insert","lines":["f"]},{"start":{"row":38,"column":76},"end":{"row":38,"column":77},"action":"insert","lines":["e"]},{"start":{"row":38,"column":77},"end":{"row":38,"column":78},"action":"insert","lines":["r"]},{"start":{"row":38,"column":78},"end":{"row":38,"column":79},"action":"insert","lines":["e"]},{"start":{"row":38,"column":79},"end":{"row":38,"column":80},"action":"insert","lines":["n"]},{"start":{"row":38,"column":80},"end":{"row":38,"column":81},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":81},"end":{"row":38,"column":82},"action":"insert","lines":[" "],"id":259},{"start":{"row":38,"column":82},"end":{"row":38,"column":83},"action":"insert","lines":["n"]},{"start":{"row":38,"column":83},"end":{"row":38,"column":84},"action":"insert","lines":["a"]},{"start":{"row":38,"column":84},"end":{"row":38,"column":85},"action":"insert","lines":["m"]},{"start":{"row":38,"column":85},"end":{"row":38,"column":86},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":42},"end":{"row":39,"column":43},"action":"remove","lines":["1"],"id":260}],[{"start":{"row":39,"column":42},"end":{"row":39,"column":43},"action":"insert","lines":["i"],"id":261},{"start":{"row":39,"column":43},"end":{"row":39,"column":44},"action":"insert","lines":["d"]}],[{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"insert","lines":["\""],"id":262}],[{"start":{"row":41,"column":55},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":263},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]},{"start":{"row":42,"column":8},"end":{"row":43,"column":0},"action":"insert","lines":["",""]},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":8},"action":"remove","lines":["    "],"id":264}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":5},"action":"insert","lines":["d"],"id":265},{"start":{"row":43,"column":5},"end":{"row":43,"column":6},"action":"insert","lines":["e"]},{"start":{"row":43,"column":6},"end":{"row":43,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":43,"column":7},"end":{"row":43,"column":8},"action":"insert","lines":[" "],"id":266},{"start":{"row":43,"column":8},"end":{"row":43,"column":9},"action":"insert","lines":["t"]},{"start":{"row":43,"column":9},"end":{"row":43,"column":10},"action":"insert","lines":["e"]},{"start":{"row":43,"column":10},"end":{"row":43,"column":11},"action":"insert","lines":["s"]},{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"insert","lines":["_"],"id":267},{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":["t"]},{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["o"]},{"start":{"row":43,"column":15},"end":{"row":43,"column":16},"action":"insert","lines":["g"]},{"start":{"row":43,"column":16},"end":{"row":43,"column":17},"action":"insert","lines":["g"]},{"start":{"row":43,"column":17},"end":{"row":43,"column":18},"action":"insert","lines":["l"]},{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["_"],"id":268},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["s"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["t"]},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["a"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["t"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["u"]},{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":43,"column":26},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":269},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":46,"column":20},"action":"insert","lines":["        item = Item(name='Create a Test')","        item.save()","        id = item.id"],"id":270}],[{"start":{"row":44,"column":8},"end":{"row":44,"column":12},"action":"remove","lines":["    "],"id":271}],[{"start":{"row":46,"column":20},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":272},{"start":{"row":47,"column":0},"end":{"row":47,"column":8},"action":"insert","lines":["        "]},{"start":{"row":47,"column":8},"end":{"row":48,"column":0},"action":"insert","lines":["",""]},{"start":{"row":48,"column":0},"end":{"row":48,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":48,"column":8},"end":{"row":48,"column":9},"action":"insert","lines":["r"],"id":273},{"start":{"row":48,"column":9},"end":{"row":48,"column":10},"action":"insert","lines":["e"]},{"start":{"row":48,"column":10},"end":{"row":48,"column":11},"action":"insert","lines":["s"]},{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":["p"]},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["o"]},{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"insert","lines":["n"]},{"start":{"row":48,"column":14},"end":{"row":48,"column":15},"action":"insert","lines":["s"]},{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":16},"end":{"row":48,"column":17},"action":"insert","lines":[" "],"id":274},{"start":{"row":48,"column":17},"end":{"row":48,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":48,"column":18},"end":{"row":48,"column":19},"action":"insert","lines":[" "],"id":275},{"start":{"row":48,"column":19},"end":{"row":48,"column":20},"action":"insert","lines":["s"]},{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["e"]},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"insert","lines":["l"]},{"start":{"row":48,"column":22},"end":{"row":48,"column":23},"action":"insert","lines":["f"]}],[{"start":{"row":48,"column":23},"end":{"row":48,"column":24},"action":"insert","lines":["."],"id":276},{"start":{"row":48,"column":24},"end":{"row":48,"column":25},"action":"insert","lines":["c"]},{"start":{"row":48,"column":25},"end":{"row":48,"column":26},"action":"insert","lines":["l"]},{"start":{"row":48,"column":26},"end":{"row":48,"column":27},"action":"insert","lines":["i"]},{"start":{"row":48,"column":27},"end":{"row":48,"column":28},"action":"insert","lines":["e"]},{"start":{"row":48,"column":28},"end":{"row":48,"column":29},"action":"insert","lines":["n"]},{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":48,"column":30},"end":{"row":48,"column":31},"action":"insert","lines":["."],"id":277},{"start":{"row":48,"column":31},"end":{"row":48,"column":32},"action":"insert","lines":["p"]},{"start":{"row":48,"column":32},"end":{"row":48,"column":33},"action":"insert","lines":["o"]},{"start":{"row":48,"column":33},"end":{"row":48,"column":34},"action":"insert","lines":["s"]},{"start":{"row":48,"column":34},"end":{"row":48,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":48,"column":35},"end":{"row":48,"column":37},"action":"insert","lines":["()"],"id":278}],[{"start":{"row":48,"column":36},"end":{"row":48,"column":38},"action":"insert","lines":["\"\""],"id":279}],[{"start":{"row":48,"column":37},"end":{"row":48,"column":38},"action":"insert","lines":["/"],"id":280},{"start":{"row":48,"column":38},"end":{"row":48,"column":39},"action":"insert","lines":["t"]},{"start":{"row":48,"column":39},"end":{"row":48,"column":40},"action":"insert","lines":["o"]},{"start":{"row":48,"column":40},"end":{"row":48,"column":41},"action":"insert","lines":["g"]},{"start":{"row":48,"column":41},"end":{"row":48,"column":42},"action":"insert","lines":["g"]},{"start":{"row":48,"column":42},"end":{"row":48,"column":43},"action":"insert","lines":["l"]},{"start":{"row":48,"column":43},"end":{"row":48,"column":44},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":44},"end":{"row":48,"column":45},"action":"insert","lines":["/"],"id":281},{"start":{"row":48,"column":45},"end":{"row":48,"column":46},"action":"insert","lines":["{"]},{"start":{"row":48,"column":46},"end":{"row":48,"column":47},"action":"insert","lines":["0"]}],[{"start":{"row":48,"column":47},"end":{"row":48,"column":48},"action":"insert","lines":["}"],"id":282}],[{"start":{"row":48,"column":49},"end":{"row":48,"column":50},"action":"insert","lines":[","],"id":283}],[{"start":{"row":48,"column":49},"end":{"row":48,"column":50},"action":"remove","lines":[","],"id":284}],[{"start":{"row":48,"column":49},"end":{"row":48,"column":50},"action":"insert","lines":["."],"id":285},{"start":{"row":48,"column":50},"end":{"row":48,"column":51},"action":"insert","lines":["f"]},{"start":{"row":48,"column":51},"end":{"row":48,"column":52},"action":"insert","lines":["o"]},{"start":{"row":48,"column":52},"end":{"row":48,"column":53},"action":"insert","lines":["r"]},{"start":{"row":48,"column":53},"end":{"row":48,"column":54},"action":"insert","lines":["m"]},{"start":{"row":48,"column":54},"end":{"row":48,"column":55},"action":"insert","lines":["a"]},{"start":{"row":48,"column":55},"end":{"row":48,"column":56},"action":"insert","lines":["t"]}],[{"start":{"row":48,"column":56},"end":{"row":48,"column":58},"action":"insert","lines":["()"],"id":286}],[{"start":{"row":48,"column":57},"end":{"row":48,"column":58},"action":"insert","lines":["i"],"id":287},{"start":{"row":48,"column":58},"end":{"row":48,"column":59},"action":"insert","lines":["d"]}],[{"start":{"row":48,"column":61},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":288},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":48,"column":61},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":289},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":49,"column":8},"end":{"row":50,"column":42},"action":"insert","lines":["        item = get_object_or_404(Item, pk=1)","        self.assertEqual(item.done, False)"],"id":290}],[{"start":{"row":49,"column":12},"end":{"row":49,"column":16},"action":"remove","lines":["    "],"id":291},{"start":{"row":49,"column":8},"end":{"row":49,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":49,"column":43},"end":{"row":49,"column":44},"action":"insert","lines":["d"],"id":292}],[{"start":{"row":50,"column":40},"end":{"row":50,"column":41},"action":"remove","lines":["e"],"id":293},{"start":{"row":50,"column":39},"end":{"row":50,"column":40},"action":"remove","lines":["s"]},{"start":{"row":50,"column":38},"end":{"row":50,"column":39},"action":"remove","lines":["l"]},{"start":{"row":50,"column":37},"end":{"row":50,"column":38},"action":"remove","lines":["a"]},{"start":{"row":50,"column":36},"end":{"row":50,"column":37},"action":"remove","lines":["F"]}],[{"start":{"row":50,"column":36},"end":{"row":50,"column":37},"action":"insert","lines":["T"],"id":294},{"start":{"row":50,"column":37},"end":{"row":50,"column":38},"action":"insert","lines":["r"]},{"start":{"row":50,"column":38},"end":{"row":50,"column":39},"action":"insert","lines":["u"]},{"start":{"row":50,"column":39},"end":{"row":50,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":26},"end":{"row":43,"column":28},"action":"insert","lines":["()"],"id":295}],[{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":[":"],"id":296}],[{"start":{"row":49,"column":42},"end":{"row":49,"column":43},"action":"remove","lines":["1"],"id":297}],[{"start":{"row":49,"column":42},"end":{"row":49,"column":43},"action":"insert","lines":["i"],"id":298}],[{"start":{"row":43,"column":27},"end":{"row":43,"column":28},"action":"insert","lines":["s"],"id":299},{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":["e"]},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["l"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["f"]}],[{"start":{"row":44,"column":25},"end":{"row":44,"column":26},"action":"remove","lines":["'"],"id":300}],[{"start":{"row":44,"column":25},"end":{"row":44,"column":26},"action":"insert","lines":["\""],"id":301}],[{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"remove","lines":["'"],"id":302}],[{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":["\""],"id":303}],[{"start":{"row":48,"column":61},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":304},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"remove","lines":["'"],"id":305}],[{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"insert","lines":["\""],"id":306}],[{"start":{"row":34,"column":39},"end":{"row":34,"column":40},"action":"remove","lines":["'"],"id":307}],[{"start":{"row":34,"column":39},"end":{"row":34,"column":40},"action":"insert","lines":["\""],"id":308}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":70},"action":"remove","lines":["response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})"],"id":309},{"start":{"row":29,"column":8},"end":{"row":29,"column":70},"action":"insert","lines":["response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})"]}],[{"start":{"row":0,"column":0},"end":{"row":51,"column":41},"action":"remove","lines":["from django.test import TestCase","from django.shortcuts import get_object_or_404","from .models import Item","","class testViews(TestCase):","    def test_get_home_page(self):","        page = self.client.get(\"/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"todo_list.html\")","        ","    def test_get_add_item_page(self):","        page = self.client.get(\"/add\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")","        ","    def test_get_edit_item_page(self):","        item = Item(name='Create a Test')","        item.save()","        ","        ","        page = self.client.get(\"/edit/{0}\".format(item.id))","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")","        ","    def test_get_edit_page_for_item_that_does_not_exist(self):","        page = self.client.get(\"/edit/1\")","        self.assertEqual(page.status_code, 404)","        ","    def test_post_create_an_item(self):","        response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})","        item = get_object_or_404(Item, pk=1)","        self.assertEqual(item.done, False)","        ","    def test_post_edit_an_item(self):","        item = Item(name=\"Create a Test\")","        item.save()","        id = item.id","        ","        response = self.client.post(\"/edit/{0}\".format(id), {\"name\": \"A different name\"})","        item = get_object_or_404(Item, pk=id)","        ","        self.assertEqual(\"A different name\", item.name)","        ","    def test_toggle_status(self):","        item = Item(name=\"Create a Test\")","        item.save()","        id = item.id","        ","        response = self.client.post(\"/toggle/{0}\".format(id))","        ","        item = get_object_or_404(Item, pk=id)","        self.assertEqual(item.done, True)"],"id":310},{"start":{"row":0,"column":0},"end":{"row":52,"column":41},"action":"insert","lines":["from django.test import TestCase","from django.shortcuts import get_object_or_404","from .models import Item","","","class TestViews(TestCase):","","    def test_get_home_page(self):","        page = self.client.get(\"/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"todo_list.html\")","    ","    def test_get_add_item_page(self):","        page = self.client.get(\"/add\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")","    ","    def test_get_edit_item_page(self):","        item = Item(name=\"Create a Test\")","        item.save()","","        page = self.client.get(\"/edit/{0}\".format(item.id))","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"item_form.html\")","    ","    def test_get_edit_page_for_item_that_does_not_exist(self):","        page = self.client.get(\"/edit/1\")","        self.assertEqual(page.status_code, 404)","    ","    def test_post_create_an_item(self):","        response = self.client.post(\"/add\", {\"name\": \"Create a Test\"})","        item = get_object_or_404(Item, pk=1)","        self.assertEqual(item.done, False)","    ","    def test_post_edit_an_item(self):","        item = Item(name=\"Create a Test\")","        item.save()","        id = item.id","","        response = self.client.post(\"/edit/{0}\".format(id), {\"name\": \"A different name\"})","        item = get_object_or_404(Item, pk=id)","","        self.assertEqual(\"A different name\", item.name)","    ","    def test_toggle_status(self):","        item = Item(name=\"Create a Test\")","        item.save()","        id = item.id","","        response = self.client.post(\"/toggle/{0}\".format(id))","","        item = get_object_or_404(Item, pk=id)","        self.assertEqual(item.done, True)"]}]]},"ace":{"folds":[],"scrolltop":1135,"scrollleft":0,"selection":{"start":{"row":53,"column":8},"end":{"row":53,"column":8},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566226441914,"hash":"b21ab61fd159503a1ab38da9621eccca9281bcf7"}