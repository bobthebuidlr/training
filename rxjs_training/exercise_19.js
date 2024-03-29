result = () => {
    var videos = [
        {
            "id": 65432445,
            "title": "The Chamber"
        },
        {
            "id": 675465,
            "title": "Fracture"
        },
        {
            "id": 70111470,
            "title": "Die Hard"
        },
        {
            "id": 654356453,
            "title": "Bad Boys"
        }
    ];

    // Expecting this output...
    // [
    //	 {
    //		 "65432445": "The Chamber",
    //		 "675465": "Fracture",
    //		 "70111470": "Die Hard",
    //		 "654356453": "Bad Boys"
    //	 }
    // ]
    return videos.
    reduce((acc, val) => {
            var obj = {};

            obj[val.id] = val.title;


            // ----- INSERT CODE TO ADD THE VIDEO TITLE TO THE ----
            // ----- NEW MAP USING THE VIDEO ID AS THE KEY	 ----

            // Object.assign() takes all of the enumerable properties from
            // the object listed in its second argument (obj) and assigns them
            // to the object listed in its first argument (accumulatedMap).
            return Object.assign(acc, obj);
        }, {});
};

console.log(result());