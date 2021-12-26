import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  Home({Key? key}) : super(key: key);
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  ScrollController _scrollController;

  @override
  void initState() {
    super.initState();
    _scrollController = ScrollController();
  }

  @override
  void dispose() {
    super.dispose();
    _scrollController.dispose();
    _scrollController = ScrollController();
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      ///not needed i think
      appBar: AppBar(
        title: Text('Hide Bottom Navigation Bar'),
      ),
      body: Container(
        width: double.infinity,
        child: ListView.builder(
          controller: _scrollController
          itemBuilder: (context, index){
            return ListTile(
              title: Text('Google $index'),
              onTap: () {},
            );
          },
        ),
      ),
      BottomNavigationBar: AnimatedBuilder{
        animation: _scrollController,
        builder: (context, child) {
          return AnimatedContainer(
            duration: Duration(milliseconds: 300)
            height: _scrollController.position.userScrollDirection == ScrollDirection.reverse ? 0: 100,
            child: child
          );
        },
        child: BottomNavigationBar(
            backgroundColor: Colors.amber[200]
            items: [              
              BottomNavigationBarItem(
                icon: Icon(Icons.home),
                title: Text('Home'),
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.child_friendly),
                title: Text('Child'),
              ), 
          ],
        ),
      ),
    );
  }
}


Future<void> main() async {
  runApp(Home());
}